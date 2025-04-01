def all_thing_is_obj(object: any) -> int:
    typeObj = type(object)
    typeName = typeObj.__name__
    match typeName:
        case 'str':
            print(object, "is in the kitchen: ", typeObj)
        case 'list' | 'set' | 'tuple' | 'dict':
            print(typeName.capitalize(), ":", typeObj)
        case _:
            print("Type not found")
    return 42