import sys

# Silverback CPU 
# Author: Emiliano Gutierrez
# Date: Decemeber 11, 2025
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# these are the opcodes - basically tells the CPU what to do
OPCODES = {
    'ADD': '00',  # adds stuff
    'SUB': '01',  # subtracts stuff
    'LDR': '10',  # grabs data from memory
    'STR': '11',  # puts data into memory
    'LW': '10',   # same as LDR just different name
    'SW': '11'    # same as STR just different name
}

# only got 4 registers so 2 bits is enough
REGS = {'R0': '00', 'R1': '01', 'R2': '10', 'R3': '11'}

def convert_to_hex(line):
    # skip empty lines and comments (handles both # and //)
    if '//' in line:
        line = line.split('//')[0].strip()
    else:
        line = line.split('#')[0].strip()
    if not line:
        return None, None

    try:
        # clean up the line and split it up
        parts = line.replace(',', ' ').split()
        mnemonic = parts[0].upper()
        
        # ADD and SUB - the math instructions
        if mnemonic in ['ADD', 'SUB']:
            # looks like: ADD R2, R0, R1
            # means R2 gets R0 + R1
            
            Rd = REGS[parts[1]]  # where the answer goes
            Rn = REGS[parts[2]]  # first number
            Rm = REGS[parts[3]]  # second number
            
            # smash it all together: opcode + dest + source1 + source2
            binary_code = OPCODES[mnemonic] + Rd + Rn + Rm
            
        # LDR/STR - memory instructions
        elif mnemonic in ['LDR', 'STR', 'LW', 'SW']:
            # looks like: LDR R0, 2
            # or could be: LDR R0, 2(R1) if you wanna get fancy
            
            Rt = REGS[parts[1]]  # which register we're using
            
            # check if they did the offset(register) thing
            if '(' in parts[2]:
                # they did the fancy version
                addr_part = parts[2]
                offset_val, Rs_part = addr_part.split('(')
                Rs = REGS[Rs_part.strip(')')]  # base register
                offset = int(offset_val)
            else:
                # just a plain number
                Rs = '00'  # default to R0 i guess
                offset = int(parts[2])
            
            # offset can only be 0-3 because we only have 2 bits for it
            if not (0 <= offset <= 3):
                return None, f"bruh offset {offset} is too big, max is 3"
            
            # turn the offset into binary
            offset_bin = format(offset, '02b')
            
            # put it together
            binary_code = OPCODES[mnemonic] + Rt + Rs + offset_bin
            
        else:
            return None, f"idk what '{mnemonic}' is supposed to be"

    except IndexError:
        return None, f"not enough stuff after '{mnemonic}'"
    except KeyError as e:
        return None, f"that register {e} doesn't exist"
    except Exception as e:
        return None, f"something broke: {e}"

    # turn the binary into hex
    hex_code = format(int(binary_code, 2), '02X')
    return hex_code, None

# --- Main Program ---
def main():
    # make sure they actually gave us file names
    if len(sys.argv) != 3:
        print("yo you gotta do: python Silverback.py <input.asm> <output.hex>")
        print("like: python Silverback.py program.asm program.hex")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # try to open the file
    try:
        with open(input_file, 'r') as f:
            assembly_code = f.readlines()
    except FileNotFoundError:
        print(f"can't find '{input_file}', check the name?")
        sys.exit(1)

    # gotta start with this header for logisim
    image_content = "v2.0 raw\n"
    
    print(f"assembling {input_file}...")
    print()
    
    # go through each line
    for line_num, line in enumerate(assembly_code, start=1):
        hex_code, error = convert_to_hex(line)
        
        if error:
            print(f"oof error on line {line_num}: {error}")
            print(f"the line was: {line.strip()}")
            sys.exit(1)
            
        if hex_code:
            image_content += f"{hex_code}\n"
            print(f"line {line_num}: {line.strip():30s} -> 0x{hex_code}")
    
    # save it
    with open(output_file, 'w') as f:
        f.write(image_content)
    
    print()
    print(f"done! saved to '{output_file}'")
    print("now just load it into the ROM in logisim and you're good")
    
if __name__ == '__main__':
    main()