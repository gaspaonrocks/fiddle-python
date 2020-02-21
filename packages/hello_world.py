# basic interactive greeting script
def helloWorld(name = "Sacha"):
    print(f"Hello, {name}")

def goodbyeWorld(name = "Sacha"):
    return f"Goodbye, {name}"

blabla = {
    "hello": helloWorld,
    "goodbye": goodbyeWorld,
    "test": "tests"
}

target1: str = "hello"
target2: str = "goodbye"

blabla["hello"]("test1")
blabla[target1]("test2")

result1 = blabla["goodbye"]("test3")
result2 = blabla[target2]("test4")

print(result1, result2)