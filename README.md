# Silverback CPU

Silverback CPU is a custom-designed single-cycle processor built in Logisim-Evolution with a bespoke 8-bit instruction set architecture (ISA) and a Python-based assembler. The project demonstrates how instructions flow through a datapath and how control signals coordinate execution in a simple CPU.

## Overview
This project implements a complete single-cycle CPU, including instruction memory, register file, ALU, data memory, and program counter. In addition to the hardware design, a custom assembler was developed to translate human-readable assembly programs into machine code executable by the CPU.

## Features
- Custom single-cycle CPU datapath implemented in Logisim-Evolution
- Four general-purpose 8-bit registers (R0–R3)
- Fixed-length 8-bit instruction encoding
- Arithmetic instructions: ADD, SUB
- Load and store instructions with base + offset addressing
- ROM for instruction memory and RAM for data memory
- Python-based assembler for assembly → machine code translation
- Demo assembly program validating correct execution

## CPU Architecture
- Single-cycle sequential datapath
- Two-read, one-write register file
- ALU supporting arithmetic operations
- Program Counter (PC) for sequential instruction execution
- Unified instruction format for simplified decoding

## Instruction Set

| Instruction | Description |
|------------|-------------|
| ADD Rd, Rn, Rm | Rd ← Rn + Rm |
| SUB Rd, Rn, Rm | Rd ← Rn − Rm |
| LDR Rt, off(Rs) | Rt ← RAM[Rs + off] |
| STR Rt, off(Rs) | RAM[Rs + off] ← Rt |

All instructions use a fixed 8-bit encoding split into four 2-bit fields:
