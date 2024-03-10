def loading_bar(percent):
    if percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{percent}% [{'%' * int(percent / 10)}{'.' * (10 - int(percent / 10))}]\nStill loading..."

percent = int(input())
print(loading_bar(percent))

