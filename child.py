# CHILD - Computational High-level Instruction Language for Dummies
# Copyright (C) 2025 RoyalPgYtPc
# GitHub: https://github.com/RoyalPgYtPc
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import re
import sys

class ChildInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.lines = []
        self.current_line = 0
        
    def error(self, message):
        print(f"Oops! Error on line {self.current_line + 1}: {message}")
        sys.exit(1)
        
    def evaluate_expression(self, expr):
        """Evaluate a mathematical or string expression"""
        expr = expr.strip()
        
        # Handle list access: listname[index]
        list_access = re.findall(r'(\w+)\[([^\]]+)\]', expr)
        for var_name, index_expr in list_access:
            if var_name in self.variables:
                index = int(self.evaluate_expression(index_expr))
                if isinstance(self.variables[var_name], list):
                    try:
                        value = self.variables[var_name][index]
                        expr = expr.replace(f'{var_name}[{index_expr}]', repr(value))
                    except IndexError:
                        self.error(f"Item {index} doesn't exist in list {var_name}")
        
        # Replace variable names with their values
        for var_name, var_value in self.variables.items():
            expr = re.sub(r'\b' + re.escape(var_name) + r'\b', repr(var_value), expr)
        
        try:
            return eval(expr)
        except Exception as e:
            self.error(f"Can't understand this expression: {expr}")
    
    def parse_condition(self, condition):
        """Parse condition statements"""
        condition = condition.strip()
        
        # Handle "is bigger than"
        if " is bigger than " in condition:
            left, right = condition.split(" is bigger than ")
            left_val = self.evaluate_expression(left)
            right_val = self.evaluate_expression(right)
            return left_val > right_val
        
        # Handle "is smaller than"
        if " is smaller than " in condition:
            left, right = condition.split(" is smaller than ")
            left_val = self.evaluate_expression(left)
            right_val = self.evaluate_expression(right)
            return left_val < right_val
        
        # Handle "is not"
        if " is not " in condition:
            left, right = condition.split(" is not ")
            left_val = self.evaluate_expression(left)
            right_val = self.evaluate_expression(right)
            return left_val != right_val
        
        # Handle "is"
        if " is " in condition:
            left, right = condition.split(" is ")
            left_val = self.evaluate_expression(left)
            right_val = self.evaluate_expression(right)
            return left_val == right_val
        
        self.error(f"Don't understand this condition: {condition}")
    
    def find_matching_end(self, start_line):
        """Find the matching 'end' for a block"""
        depth = 1
        i = start_line + 1
        while i < len(self.lines):
            line = self.lines[i].strip()
            if line.startswith(('if ', 'repeat ', 'count ', 'learn ')):
                depth += 1
            elif line == 'end' or line == 'otherwise':
                depth -= 1
                if depth == 0:
                    return i
                depth += 1  # 'otherwise' keeps the same depth
            i += 1
        self.error("Missing 'end' statement")
    
    def find_otherwise(self, if_line):
        """Find 'otherwise' clause if it exists"""
        depth = 1
        i = if_line + 1
        while i < len(self.lines):
            line = self.lines[i].strip()
            if line.startswith(('if ', 'repeat ', 'count ', 'learn ')):
                depth += 1
            elif line == 'otherwise':
                if depth == 1:
                    return i
            elif line == 'end':
                depth -= 1
                if depth == 0:
                    return None
            i += 1
        return None
    
    def execute_block(self, start_line, end_line):
        """Execute a block of code"""
        saved_line = self.current_line
        self.current_line = start_line
        while self.current_line < end_line:
            self.execute_line(self.lines[self.current_line])
            self.current_line += 1
        self.current_line = saved_line
    
    def execute_line(self, line):
        """Execute a single line of CHILD code"""
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('//'):
            return None
        
        # SAY command (output)
        if line.startswith('say '):
            content = line[4:].strip()
            value = self.evaluate_expression(content)
            print(value)
            return None
        
        # REMEMBER command (variable assignment)
        if line.startswith('remember ') and ' as ' in line:
            parts = line[9:].split(' as ')
            if len(parts) != 2:
                self.error("Use 'remember VALUE as NAME'")
            value_expr = parts[0].strip()
            var_name = parts[1].strip()
            self.variables[var_name] = self.evaluate_expression(value_expr)
            return None
        
        # LIST command (create a list)
        if line.startswith('list ') and ' as ' in line:
            parts = line[5:].split(' as ')
            if len(parts) != 2:
                self.error("Use 'list [item1, item2, ...] as NAME'")
            list_expr = parts[0].strip()
            var_name = parts[1].strip()
            self.variables[var_name] = self.evaluate_expression(list_expr)
            return None
        
        # ADD TO LIST command
        if line.startswith('add ') and ' to ' in line:
            parts = line[4:].split(' to ')
            if len(parts) != 2:
                self.error("Use 'add VALUE to LISTNAME'")
            value_expr = parts[0].strip()
            list_name = parts[1].strip()
            if list_name not in self.variables:
                self.error(f"List '{list_name}' doesn't exist")
            if not isinstance(self.variables[list_name], list):
                self.error(f"'{list_name}' is not a list")
            value = self.evaluate_expression(value_expr)
            self.variables[list_name].append(value)
            return None
        
        # GET FROM LIST command
        if line.startswith('get item ') and ' from ' in line and ' as ' in line:
            parts = line[9:].split(' from ')
            index_expr = parts[0].strip()
            rest = parts[1].split(' as ')
            list_name = rest[0].strip()
            var_name = rest[1].strip()
            
            if list_name not in self.variables:
                self.error(f"List '{list_name}' doesn't exist")
            if not isinstance(self.variables[list_name], list):
                self.error(f"'{list_name}' is not a list")
            
            index = int(self.evaluate_expression(index_expr))
            try:
                self.variables[var_name] = self.variables[list_name][index]
            except IndexError:
                self.error(f"Item {index} doesn't exist in list {list_name}")
            return None
        
        # SIZE OF LIST command
        if line.startswith('size of ') and ' as ' in line:
            parts = line[8:].split(' as ')
            list_name = parts[0].strip()
            var_name = parts[1].strip()
            
            if list_name not in self.variables:
                self.error(f"List '{list_name}' doesn't exist")
            if not isinstance(self.variables[list_name], list):
                self.error(f"'{list_name}' is not a list")
            
            self.variables[var_name] = len(self.variables[list_name])
            return None
        
        # ASK command (input)
        if line.startswith('ask ') and ' and remember it as ' in line:
            parts = line[4:].split(' and remember it as ')
            if len(parts) != 2:
                self.error("Use 'ask \"question\" and remember it as NAME'")
            prompt = self.evaluate_expression(parts[0].strip())
            var_name = parts[1].strip()
            user_input = input(str(prompt) + " ")
            # Try to convert to number if possible
            try:
                user_input = float(user_input)
                if user_input.is_integer():
                    user_input = int(user_input)
            except:
                pass
            self.variables[var_name] = user_input
            return None
        
        # IF command with OTHERWISE
        if line.startswith('if ') and ' then' in line:
            condition = line[3:line.index(' then')].strip()
            otherwise_line = self.find_otherwise(self.current_line)
            end_line = self.find_matching_end(self.current_line)
            
            if self.parse_condition(condition):
                # Execute the if block
                if otherwise_line:
                    self.execute_block(self.current_line + 1, otherwise_line)
                else:
                    self.execute_block(self.current_line + 1, end_line)
                self.current_line = end_line
            else:
                # Execute the otherwise block if it exists
                if otherwise_line:
                    self.execute_block(otherwise_line + 1, end_line)
                self.current_line = end_line
            return None
        
        # OTHERWISE command (handled by IF)
        if line == 'otherwise':
            return None
        
        # REPEAT command
        if line.startswith('repeat ') and ' times' in line:
            times_expr = line[7:line.index(' times')].strip()
            times = int(self.evaluate_expression(times_expr))
            end_line = self.find_matching_end(self.current_line)
            
            for _ in range(times):
                self.execute_block(self.current_line + 1, end_line)
            
            self.current_line = end_line
            return None
        
        # COUNT command (for loop)
        if line.startswith('count from ') and ' to ' in line and ' as ' in line:
            parts = line[11:].split(' to ')
            start_expr = parts[0].strip()
            rest = parts[1].split(' as ')
            end_expr = rest[0].strip()
            var_name = rest[1].strip()
            
            start = int(self.evaluate_expression(start_expr))
            end = int(self.evaluate_expression(end_expr))
            end_line = self.find_matching_end(self.current_line)
            
            for i in range(start, end + 1):
                self.variables[var_name] = i
                self.execute_block(self.current_line + 1, end_line)
            
            self.current_line = end_line
            return None
        
        # FOR EACH command (iterate through list)
        if line.startswith('for each item in ') and ' as ' in line:
            parts = line[17:].split(' as ')
            list_name = parts[0].strip()
            var_name = parts[1].strip()
            
            if list_name not in self.variables:
                self.error(f"List '{list_name}' doesn't exist")
            if not isinstance(self.variables[list_name], list):
                self.error(f"'{list_name}' is not a list")
            
            end_line = self.find_matching_end(self.current_line)
            
            for item in self.variables[list_name]:
                self.variables[var_name] = item
                self.execute_block(self.current_line + 1, end_line)
            
            self.current_line = end_line
            return None
        
        # LEARN command (define function)
        if line.startswith('learn how to '):
            func_signature = line[13:].strip()
            
            # Parse function name and parameters
            if ' with ' in func_signature:
                func_name, params = func_signature.split(' with ')
                param_list = [p.strip() for p in params.split(' and ')]
            else:
                func_name = func_signature
                param_list = []
            
            end_line = self.find_matching_end(self.current_line)
            
            # Store function definition
            self.functions[func_name] = {
                'params': param_list,
                'start': self.current_line + 1,
                'end': end_line
            }
            
            self.current_line = end_line
            return None
        
        # DO command (call function)
        if line.startswith('do '):
            func_call = line[3:].strip()
            
            # Parse function name and arguments
            if ' with ' in func_call:
                func_name, args = func_call.split(' with ')
                arg_list = [self.evaluate_expression(a.strip()) for a in args.split(' and ')]
            else:
                func_name = func_call
                arg_list = []
            
            if func_name not in self.functions:
                self.error(f"Don't know how to '{func_name}'")
            
            func_def = self.functions[func_name]
            
            if len(arg_list) != len(func_def['params']):
                self.error(f"'{func_name}' needs {len(func_def['params'])} things, but got {len(arg_list)}")
            
            # Save current variables and set parameters
            saved_vars = self.variables.copy()
            for param, arg in zip(func_def['params'], arg_list):
                self.variables[param] = arg
            
            # Execute function body
            self.execute_block(func_def['start'], func_def['end'])
            
            # Restore variables (keep new/modified ones)
            for var in list(self.variables.keys()):
                if var not in func_def['params'] and var in saved_vars:
                    continue
                elif var in func_def['params']:
                    del self.variables[var]
            
            return None
        
        # END command (handled by other constructs)
        if line == 'end':
            return None
        
        # Unknown command
        self.error(f"Don't understand this command: {line}")
    
    def run(self, code):
        """Run CHILD code"""
        self.lines = code.split('\n')
        self.current_line = 0
        
        while self.current_line < len(self.lines):
            self.execute_line(self.lines[self.current_line])
            self.current_line += 1


# Example usage
if __name__ == "__main__":
    interpreter = ChildInterpreter()
    
    # Example program showcasing new features
    example_code = """
// Welcome to CHILD Language!
say "=== CHILD Language Demo ==="
say ""

// Testing IF and OTHERWISE
say "Testing IF and OTHERWISE:"
remember 15 as age
if age is bigger than 12 then
    say "You're a teenager or older!"
otherwise
    say "You're a kid!"
end
say ""

// Testing LISTS
say "Testing LISTS:"
list [10, 20, 30, 40, 50] as numbers
say "My list of numbers:"
say numbers

add 60 to numbers
say "After adding 60:"
say numbers

get item 0 from numbers as firstNumber
say "The first number is:"
say firstNumber

size of numbers as howMany
say "The list has this many items:"
say howMany
say ""

// Testing FOR EACH loop
say "Printing each number:"
for each item in numbers as num
    say num
end
say ""

// Testing FUNCTIONS
say "Testing FUNCTIONS:"
learn how to greet with name
    say "Hello, "
    say name
    say "Nice to meet you!"
end

do greet with "Alice"
say ""

learn how to add with a and b
    remember a + b as result
    say "The sum is:"
    say result
end

do add with 5 and 7
say ""

// More complex function
learn how to countdown with start
    count from start to 1 as i
        say i
    end
    say "Blastoff!"
end

say "Countdown from 5:"
do countdown with 5
"""
    
    print("Running CHILD Program...\n")
    interpreter.run(example_code)
    
    print("\n\n=== Usage Info ===")
    print("Save your code as a .child file and run:")
    print("  python child.py myprogram.child")