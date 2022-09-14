def testing_scope():
    def local_var():
        foo = 'local'
        print(id(foo))

    def nonlocal_var():
        nonlocal foo
        foo = 'nonlocal'
        print(id(foo))

    def global_var():
        global foo
        foo = 'global'
        print(id(foo))

    foo = 'testing'
    print(id(foo))
    local_var()
    print('local ---->', foo, id(foo))
    nonlocal_var()
    print('nonlocal ---->', foo, id(foo))
    global_var()
    print('global ---->', foo, id(foo))

testing_scope()
print('in global ---->', foo, id(foo))
