def join_with_hyphen(*args):
    if not args:
        return ""
        
    return "-".join(args)


print(join_with_hyphen("Python", "is", "awesome"))  

print(join_with_hyphen("Code", "Master"))          

print(join_with_hyphen())