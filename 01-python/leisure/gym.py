def draw_gym(type = "treadmill"):
    listType = ["dumbbell", "treadmill"]
    if type not in listType:
        print("gym not found")
        return
    print("========")
    print()
    if type == "dumbbell":
        print("||--||")
        print("||--||")
        print("||--||")
    if type == "treadmill":
        print("     @        |")
        print("  /\ |   /    /")
        print(" /   | \/    /")
        print("    / \     /")
        print("   /  /    /")
        print("==========/")
    print("")
    print("========")
    return
