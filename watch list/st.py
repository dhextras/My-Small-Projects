import json
from time import sleep

class Store:
    # Add
    def add(d, t):
        # loading data....
        with open("st.json") as f:
            data = json.load(f)
        t = "Movie" if t=="m" else "Series"

        # checking if its already there.
        search = "Not Found"
        for i in data[t]:
            if str(i["Name"]) == str(d["Name"]):
                search = "found"
                print("Found it.")
                f_str = f"{t} {d} is already in the file"
                break
            else:
                print('.')
                sleep(0.1)

        if search == "Not Found":
            # load and dumping data to file....
            print("\nNot found...")
            data[t].append(d)

            with open("st.json", "w") as f:
                json.dump(data, f, indent=4)
            f_str = f"{t} {d} has been dumped to the file."

        return print(f_str + '\n')

    # change
    def change(n, n_s, n_t):
        # extract the data from file.
        with open("st.json") as f:
            data = json.load(f)

        search = "Run"
        while search == "Run":
            n_t = "Movie" if n_t=="m" else "Series"

            for j in data[n_t]:
                # check if its there
                if str(j["Name"]) == str(n):
                    o_s = j["State"]
                    print("\nFound it")

                    # avoid changing the same thing.
                    if str(o_s) == str(n_s):
                        f_str = "But Theres no difference in the old and new state u gave."
                    else:
                        j["State"] = n_s
                        # load & dump data to file
                        with open("st.json", "w") as f:
                            json.dump(data, f, indent=4)
                        f_str = f"State of the {n} has been changed from {o_s} to {n_s}."

                    # break if its found
                    search = "Found"
                    break
                else:
                    print(".")
                    sleep(0.1)

                # return if its not in the data
                search = "not_found"
                f_str = f"Cant find {n} in the database.\nDumping it to the data base......"
                
        if search == "not_found":
            # load & dump data to file
            obj = {"Name": n, "State": n_s}
            data[n_t].append(obj)
            with open("st.json", "w") as f:
                json.dump(data, f, indent=4)

        return print(f'\n{f_str}')

    # read
    def read(ltr1, ltr2, t, s):
        list1 = []

        # extract the data from file.
        with open("st.json", "r") as f:
            data = json.load(f)
        
        # sorting out depends on the *(Type) 
        if t == "m":
            var1 = data["Movie"]
        elif t == "s":
            var1 = data["Series"]
        else:
            for i in ["Series", "Movie"]:
                list1.append({"Name": f'\n {-1*" "}{i}:', "State": ""})
                for j in data[i]:
                    list1.append(j)
            var1 = list1

        # ignore, this just for clean look
        print(f'\n  Name{43*" "}  State')
        print(f' ======{43*" "}=======')

        n = 0
        # sorting out depends on the *(State, by 1st letter)
        for a in var1:
            # l is just for space formatting, just ignore these variables
            l = (int(48 - len(str(a["Name"])))*" ")
            pin = '📎 ' if a['Name'][-1] != ':' else ''
            list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            # this are bold, italic ANSI escape-sequance.
            bold, italic, close = '\x1B[1m', '\x1B[3m', '\x1B[0m'
            name_state = f"  {pin}{a['Name']}{l}{bold}{a['State'].upper()}{close}"
            type = f"  {bold}{pin}{a['Name']}{close}"

            # extracting the asked data and printing out, this nested if Statement sucks it's too hard to explain it.
            # hope u can figure it out. its work fine by the way. Pls let me know if i could actually make this more readable. {telegram - @I_Yuji}
            if ltr1 == "n":
                if s == "n" or s == "u" or  s == "w":
                    if str(a["State"]) == str(s):
                        n+=1; print(name_state)
                    elif a['Name'][-1] == ':':
                        print(type)
                elif a['Name'][-1] == ':':
                    print(type)
                else:
                    n+=1; print(name_state)
            else:
                if ltr2 == "null":
                    if a['Name'][0] in list2:
                        continue
                    elif a['Name'][-1] == ':':
                        print(type)
                    else:
                        if s == "n" or s == "u" or  s == "w":
                            if str(a["State"]) == str(s):
                                n+=1; print(name_state)
                        else:
                            n+=1; print(name_state)
                else:
                    if a['Name'][0] == ltr2:
                        if s == "n" or s == "u" or  s == "w":
                            if str(a["State"]) == str(s):
                                n+=1; print(name_state)
                        else:
                            n+=1; print(name_state)
                    elif a['Name'][-1] == ':':
                        print(type)
                    else: continue

        return print('\nThis is all i found.') if n >= 1 else print('\nLooks like theres nothing matching ur selection.')

# help
class Help:
        # template ignore this is just for clean look at the border
        def template(first_dscrpt, opt_dict, head, final_dscrpt,k):
            print(k+first_dscrpt)

            print(f'\n      {head}{46*" "} Discriptions')
            print(f'    ========={43*" "}================\n')

            # Looping through the flags and discriptions.
            for i in opt_dict:
                j = opt_dict[str(i)]
                print(f'{i}{(55-len(i))*" "}* {j}\n')

            print(f"\n{final_dscrpt}\n")
        
        # run
        def run(a):
            # default
            first_dscrpt = "* Here are the all valid inputs and flags and their functions."
            final_dscrpt = "This is it. pls avoid only adding numbers as name and if u wanna exit on mid way just leave empty and hit enter. simple right."
            head = "Input"
            opt_dict = {
                "   ['M'/'S']": "Type: this define the type of the show your entering.", 
                "      'M'": "M stand for Movies.",
                "      'S'": "S stand for Series.",
                "   ['W'/'N'/'U']": "State: this define the current state of it.", 
                "      'W'": "W stand for Watched.",
                "      'N'": "N stand for not Finished/Relesed.",
                "      'U'": "U stand for Unbegun ones."
            }
            k = f"Argument '{a}' Found.\n\n"

            # change default depends on the user input.
            if a == "add":
                #all the defaults will same for this so no need to change this at all 
                pass
            elif a == "change":
                for i in ["   ['M'/'S']", "      'M'", "      'S'"]:
                    del opt_dict[i]
            elif a == "read":
                opt_dict = {
                    "   ['Y'/' ']": "This is to sort the list by 1st letter or not.",
                    "      'Y'": "Y stand for yes.",
                    "      ' '": "Leave empty to skip sorting out by letter.",
                    "   ['Any Letter'/' ']": "Letters: this define the letter you gone a sort out by",
                    "      'Any Letter'": "Eneter the first letter to sort out.",
                    "      '  '": "Leave empty for different charector or numbers.",
                    "   ['M'/'S'/' ']": "Type: this define the type of the show your entering.",
                    "      'M'": "M stand for Movies.",
                    "      'S'": "S stand for Series.",
                    '      " "': "Leave empty for no filters.",
                    "   ['W'/'N'/'U'/' ']": "State: this define the current state of it.", 
                    "      'W'": "W stand for Watched.",
                    "      'N'": "N stand for not Finished/Relesed.",
                    "      'U'": "U stand for Unbegun ones.",
                    '      "  "': "Leave empty for no filters."
                }
                
                final_dscrpt = "Thats it. Unlike the other cases use '0' as a input if u want to exit in mid way.\nBecause if the input is non it will continue with no filter option."
            else:
                j = f"Argument '{a}' Not found" if a != "h" else "No Argument detected."
                k = f"{j}\nAvailable: ['Add', 'Change', 'Read']\n\n"
                final_dscrpt = f"This is simply it, If you want more specific explantion on a specific flags run these.\n:~$ bash st -h Add\n:~$ bash st -h change\nAvailable arguments: ['Add'/'Change'/'Read']\n\nNote:\n* The cases doesn't matter for arguments 'Add/add/ADD/AdD' All same.\n* But for flags its important '-h'/'-H' 2 different things.\n* Runnig more then one flag is also not gone a work."
                head = "Flags"
                opt_dict = {
                    "      -h": "Help: for getting help on flags and inputs.",
                    "      -a": "Add: to add new Movie/Series",
                    "      -c": "Change: to change the status of the Movie/Series.",
                    "      -r": "Read: to sort out and list1 the Movies/Series in various way."
                }

            # pass these vars to the template
            return Help.template(first_dscrpt, opt_dict, head, final_dscrpt, k)

# Checking the os to avoid error with lolcat.
if __name__ == '__main__':
    import platform
    print(platform.system().lower())