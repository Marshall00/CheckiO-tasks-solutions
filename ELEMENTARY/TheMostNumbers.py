def checkio(*args):
    if args:
        minimum=min(args)
        maximum=max(args)
        return maximum-minimum
    else:
        return 0