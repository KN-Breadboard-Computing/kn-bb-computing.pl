from typing import List
import json

def distinct_arguments(arguments: List[str]) -> List[str]:
    result = []
    for argument in arguments:
        if argument not in result:
            result.append(argument)

    return result

def translate_argument(argument_name: str) -> str:
    if argument_name == 'A':
        return ['REG8', ['value from 8 bit register', '8 bit register']]
    elif argument_name == 'B':
        return ['REG8', ['value from 8 bit register', '8 bit register']]
    elif argument_name == 'F':
        return ['REG8', ['value from 8 bit register', '8 bit register']]
    elif argument_name == 'INT':
        return ['REG8', ['value from 8 bit register', '8 bit register']]
    elif argument_name == 'TH':
        return ['REG8', ['value from 8 bit register', '8 bit register']]
    elif argument_name == 'TL':
        return ['REG8', ['value from 8 bit register', '8 bit register']]
    elif argument_name == 'T':
        return ['REG16', ['value from 16 bit register', '16 bit register']]
    elif argument_name == 'CONST':
        return ['CONST8', ['8 bit constant', 'FORBIDDEN']]
    elif argument_name == 'MEM8':
        return ['MEM8', ['value from memory at 8 bit address', 'memory at 8 bit address']]
    elif argument_name == 'MEM16':
        return ['MEM16', ['value from memory at 16 bit address', 'memory at 16 bit address']]
    elif argument_name == 'MEM':
        return ['MEM16', ['value from memory at 16 bit address', 'memory at 16 bit address']]
    elif argument_name == 'MEMZP':
        return ['MEM8', ['value from memory at 8 bit address', 'memory at 8 bit address']]
    elif argument_name == 'STC':
        return ['STC', ['value from top of the stack', 'top of the stack']]
    else:
        print('ERROR: Unknown argument name', argument_name)
        return None
    
def translate_operation(operation_name: str) -> str:
    if operation_name == 'NEG':
        return 'negation of'
    elif operation_name == 'MUL2':
        return 'multiplication by 2 of'
    elif operation_name == 'DIV2':
        return 'division by 2 of'
    elif operation_name == 'INV':
        return 'inversion of'
    elif operation_name == 'SHR':
        return 'shift right of'
    elif operation_name == 'SHL':
        return 'shift left of'
    elif operation_name == 'ADD':
        return 'addition of'
    elif operation_name == 'SUB':
        return 'subtraction of'
    elif operation_name == 'OR':
        return 'bitwise OR of'
    elif operation_name == 'AND':
        return 'bitwise AND of'
    elif operation_name == 'XOR':
        return 'bitwise XOR of'
    else:
        print('ERROR: Unknown operation name', operation_name)
        return None
    
def translate_arguments(arguments: List[str]) -> List[str]:
    return [translate_argument(argument) for argument in arguments]

def parse_arguments(arguments: List[str]) -> List[str]:
    parsed_arguments = [''] * len(arguments)
    for index in range(len(parsed_arguments)):
        for argument in arguments[index]:
            parsed_arguments[index] = str(argument[0]) if parsed_arguments[index] == '' else f'{parsed_arguments[index]}/{argument[0]}'
    
    return parsed_arguments

def export_instructions(file: any, mnemonic: str, arguments: List[str], 
                        description: str) -> None:
    file.write(
        f"""
        "{key}": {{
            "mnemonic": "{mnemonic}",
            "arguments":"{', '.join(f'{arg}' for arg in arguments)}",
            "description": "{description}"
        }},
        """
    )


if __name__ == '__main__':
    instructions_dict = {}
    with open('static/all-instructions.json', 'r') as f:
        instructions = json.load(f)
        
        for instruction_name in instructions:
            instruction = instructions[instruction_name]
            mnemonic = instruction['mnemonic']
            if mnemonic not in instructions_dict:
                instructions_dict[mnemonic] = [translate_arguments(instruction['arguments'])]
            else:
                instructions_dict[mnemonic].append(translate_arguments(instruction['arguments']))

    with open('static/general-instructions.json', 'w') as f:
        f.write('{')

        for key, value in instructions_dict.items():
            if key == 'MOV':
                available_arguments = [[], []]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                    available_arguments[1].append(args[1])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Move constant or value from memory or value from register to register')
            elif key == 'MOVAT':
                available_arguments = [[], []]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                    available_arguments[1].append(args[1])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Move constant or value from register to memory at some address')
            elif key in ['NEG', 'MUL2', 'DIV2', 'INV', 'SHR', 'SHL']:
                available_arguments = [[], []]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                    available_arguments[1].append(args[1])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Calculate {translate_operation(key)} value from register and store it in register, memory or stack')
            elif key in ['ADD', 'OR', 'AND', 'XOR']:
                available_arguments = [[]]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Calculate {translate_operation(key)} REG_A with REG_B and store it in register, memory or stack')
            elif key == 'SUB':
                available_arguments = [[], [], []]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                    available_arguments[1].append(args[1])
                    available_arguments[2].append(args[2])
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Calculate {translate_operation(key)} values from registers and store it in register, memory or stack')
            elif key == 'CMP':
                available_arguments = [[], []]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                    available_arguments[1].append(args[1])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Compare values from given registers and store result in REG_F')
            elif key == 'CLR':
                available_arguments = [[]]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Clear given register')
            elif key == 'INC':
                available_arguments = [[]]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Increment given register')
            elif key == 'DEC':
                available_arguments = [[]]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Decrement given register')
            elif key == 'JMPIMM':
                available_arguments = [[]]
                for args in distinct_arguments(value):
                    if len(args) > 0:
                        available_arguments[0].append(args[0])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Jump directly to address given by constant or value from register')
            elif key == 'JMPREL':
                available_arguments = [[]]
                for args in distinct_arguments(value):
                    if len(args) > 0:
                        available_arguments[0].append(args[0])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Jump relative with offset given by constant or value from register or memory')
            elif key == 'PUSH':
                available_arguments = [[]]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Push constant, value from register or memory to stack')
            elif key == 'POP':
                available_arguments = [[]]
                for args in distinct_arguments(value):
                    available_arguments[0].append(args[0])
                available_arguments = [distinct_arguments(args) for args in available_arguments]
                export_instructions(f, key, parse_arguments(available_arguments), 
                                    f'Pop value from stack to register or memory')
                
            elif key == 'HALT':
                export_instructions(f, key, ['-'], f'Halt the program')
            elif key == 'NOP':
                export_instructions(f, key, ['-'], f'Do nothing for one cycle')
            elif key == 'SKIP':
                export_instructions(f, 'SKIP/SKIP1/SKIP2', ['-'], f'Skip current/next/next two program instructions')
            elif key == 'SKIP1' or key == 'SKIP2':
                pass # processed in SKIP
            elif key == 'ISR':
                export_instructions(f, key, ['-'], f'Push program counter to stack, set program counter to address of interrupt service routine and start interrupt service routine')
            elif key == 'IRET':
                export_instructions(f, key, ['-'], f'Pop program counter from stack and exit interrupt service routine')
            else:
                print('ERROR: Unknown instruction', key)
            
        f.write('}')

    file_content = ''
    with open('static/general-instructions.json', 'r') as f:
        file_content = f.read()
    
    file_content = ''.join(file_content.rsplit(',', 1))

    with open('static/general-instructions.json', 'w') as f:
        f.write(file_content)
        
    