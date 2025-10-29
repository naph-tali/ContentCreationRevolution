#  SYNTAX VALIDATION SCRIPT
# Check all Python files for syntax errors

import os
import sys
import ast

def validate_python_file(file_path):
    """Validate Python file syntax"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Parse the AST to check for syntax errors
        ast.parse(source_code)
        return True, " Valid syntax"
        
    except SyntaxError as e:
        return False, f" Syntax error: {e}"
    except UnicodeDecodeError as e:
        return False, f" Encoding error: {e}"
    except Exception as e:
        return False, f" Other error: {e}"

def validate_all_files():
    """Validate all Python files in the project"""
    python_files = []
    
    # Find all Python files
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(" VALIDATING ALL PYTHON FILES...")
    print("=" * 50)
    
    all_valid = True
    for file_path in python_files:
        is_valid, message = validate_python_file(file_path)
        status = "PASS" if is_valid else "FAIL"
        print(f"{status}: {file_path}")
        if not is_valid:
            print(f"     {message}")
            all_valid = False
    
    return all_valid

if __name__ == "__main__":
    all_valid = validate_all_files()
    
    print("\\n" + "=" * 50)
    if all_valid:
        print("ðŸŽ‰ ALL FILES HAVE VALID SYNTAX!")
        print("ðŸš€ Ready for cosmic operations!")
    else:
        print("  Some files have syntax issues")
        print("ðŸ”§ Please fix the reported errors")
    
    sys.exit(0 if all_valid else 1)
