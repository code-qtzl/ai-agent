import sys

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file

# from call_functions import available_functions

# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
# from functions.run_python import run_python_file

# === Testing with schema_get_files_info ===
# from functions.get_files_info import get_files_info



#     """Test the get_files_info function"""
# def test_get_files_info():

#     resultCurrent = get_files_info("calculator", ".")
#     print("Result for current directory:")
#     print(resultCurrent)
#     print()

#     resultPKG = get_files_info("calculator", "pkg")
#     print("Result for pkg directory:")
#     print(resultPKG)
#     print()

#     resultBIN = get_files_info("calculator", "/bin")
#     print("Result for bin directory:")
#     print(resultBIN)
#     print()

#     resultLvlUp = get_files_info("calculator", "../")
#     print("Result for '../' directory:")
#     print(resultLvlUp)
#     print()

# if __name__ == "__main__":
#     test_get_files_info()


#     """Test the get_file_content function"""
# def test_get_file_content():
#     resultCurrent = get_file_content("calculator", "main.py")
#     print("Result for current directory:")
#     print(resultCurrent)
#     print()

#     resultPKG = get_file_content("calculator", "pkg/calculator.py")
#     print("Result for pkg directory:")
#     print(resultPKG)
#     print()

#     resultBIN = get_file_content("calculator", "bin/cat")
#     print("Result for bin directory:")
#     print(resultBIN)
#     print()

#     resultLvlUp = get_file_content("calculator", "pkg/does_not_exist.py")
#     print("Result for '../' directory:")
#     print(resultLvlUp)
#     print()

# if __name__ == "__main__":
#     test_get_file_content()


# """Test the write_file function"""
# def test_write_file():
#     resultCurrent = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#     print("Result for writing to current directory:")
#     print(resultCurrent)
#     print()

#     resultPKG = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#     print("Result for writing to pkg directory:")
#     print(resultPKG)
#     print()

#     resultBIN = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#     print("Result for writing to temp directory:")
#     print(resultBIN)
#     print()

# if __name__ == "__main__":
#   test_write_file()


#     """Test the run_python_file function"""
# def test_run_python_file():
#     resultCurrent = run_python_file("calculator", "main.py")
#     print("Result for running main.py in current directory:")
#     print(resultCurrent)
#     print()

#     resultPKG = run_python_file("calculator", "pkg/main.py", ["5", "3"])
#     print("Result for running main.py in pkg directory with args 5 and 3:")
#     print(resultPKG)
#     print()

#     resultBIN = run_python_file("calculator", "tests.py")
#     print("Result for running tests.py in bin directory:")
#     print(resultBIN)
#     print()

#     resultLvlUp = run_python_file("calculator", "../main.py")
#     print("Result for running ../main.py in pkg directory:")
#     print(resultLvlUp)
#     print()

#     resultLvlUp = run_python_file("calculator", "nonexistent.py")
#     print("Result for running nonexistent.py in pkg directory:")
#     print(resultLvlUp)
#     print()

# if __name__ == "__main__":
#   test_run_python_file()


# Test the get_files_info function -> Directory listing functionality
# def test_get_files_info():
#     resultCurrent = get_files_info({'directory': '.'})
#     print("Result for current directory:")
#     print(resultCurrent)
#     print()

#     resultPKG = get_files_info({'directory': 'pkg'})
#     print("Result for pkg directory:")
#     print(resultPKG)
#     print()

# if __name__ == "__main__":
#     test_get_files_info()


# def test_files_content():
#     resultCurrent = get_file_content({'file_path': 'main.py'})
#     print("Result for main.py:")
#     print(resultCurrent)
#     print()

#     resultPKG = write_file({'file_path': 'main.txt', 'content': 'hello'})
#     print("Result for writing 'hello' to main.txt:")
#     print(resultPKG)
#     print()

#     resultBIN = run_python_file({'file_path': 'main.py'})
#     print("Result for running main.py:")
#     print(resultBIN)
#     print()

#     resultLvlUp = get_files_info({'directory': 'pkg'})
#     print("Result for listing content in pkg directory:")
#     print(resultLvlUp)
#     print()


# def test_direct_function_calls():
#     resultOne = run_python_file("directory", "main.py")
#     print("Result for running main.py in directory:")
#     print(resultOne)
#     print()

#     resultTwo = get_file_content({'file_path': 'main.py'})
#     print("Result for main.py:")
#     print(resultTwo)
#     print()

#     resultThree = write_file({'file_path': 'main-greeting.txt', 'content': 'hello world'})
#     print("Result for writing 'hello world' to main-greeting.txt:")
#     print(resultThree)
#     print()

#     resultFour = run_python_file("calculator", "tests.py")
#     print("Result for running tests.py in calculator:")
#     print(resultFour)
#     print()


# if __name__ == "__main__":
#     test_direct_function_calls()


# def test_direct_function_calls():
#     """Test direct function calls to ensure they work correctly"""
#     print(f"\n{'='*60}")
#     print("DIRECT FUNCTION TESTS")
#     print(f"{'='*60}")
    
#     # Test get_files_info
#     print("\n1. Testing get_files_info (current directory):")
#     result = get_files_info({'directory': '.'})
#     print(f"Result: {result}")
    
#     # Test get_files_info for calculator directory
#     print("\n2. Testing get_files_info (calculator directory):")
#     result = get_files_info({'directory': 'calculator'})
#     print(f"Result: {result}")
    
#     # Test get_file_content
#     print("\n3. Testing get_file_content (main.py):")
#     result = get_file_content({'file_path': 'main.py'})
#     print(f"Result: {result[:200]}..." if len(str(result)) > 200 else f"Result: {result}")
    
#     # Test write_file
#     print("\n4. Testing write_file:")
#     result = write_file({'file_path': 'direct_test.txt', 'content': 'Direct function test content'})
#     print(f"Result: {result}")
    
#     # Test run_python_file
#     print("\n5. Testing run_python_file (calculator tests):")
#     result = run_python_file({'file_path': 'calculator/tests.py'})
#     print(f"Result: {result}")

# if __name__ == "__main__":
#     test_direct_function_calls()




#     """Test the get_file_content function"""
# def new_test():
#     resultCurrent = run_python_file(".", "main.py")
#     print("Result for current directory:")
#     print(resultCurrent)
#     print()

#     resultPKG = get_file_content(".", "lorem.txt")
#     print("Content from lorem:")
#     print(resultPKG)
#     print()

#     resultBIN = write_file(".", "/calculator", "# calculator")
#     print("Creating new ReadMe")
#     print(resultBIN)
#     print()

#     resultLvlUp = get_files_info(".", "main.py")
#     print("What files are in root")
#     print(resultLvlUp)
#     print()

# if __name__ == "__main__":
#     new_test()


def test():
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    test()
