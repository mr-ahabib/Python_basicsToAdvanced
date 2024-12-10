greetings=" Hello, world! "

print(greetings)
print(len(greetings))
print(greetings[0])


#check in the sentence

print("Hello" in greetings)


#slicing
print(greetings[2:5])

print(greetings[:5])
print(greetings[2:])


print(greetings[-5:-2])


#lower/upper


print(greetings.lower())

print(greetings.upper())

#remove space from first and last
print(greetings.strip())

#replace
print(greetings.replace("Hello", "Hi"))
print(greetings.replace("world!","everyone. I am Habib."))


#concatenetion
name="Habib"
position="student"

print(name +":"+position)

#formatted string
print(f"I am {name} and I am a {position}")