import datetime

events = {}


def add_event(name, date, st_time, end_time, location, description):
    event_id = len(events) + 1
    
    while True:
        overlap = False
        for existing_event in events.values():
            if existing_event['location'] == location and existing_event['date'] == date:
                event_start_time = time_convert(existing_event['st_time'])
                event_end_time = time_convert(existing_event['end_time'])
                new_start_time = time_convert(st_time)
                new_end_time = time_convert(end_time)
                if check_overlap(event_start_time, event_end_time, new_start_time, new_end_time):
                    overlap = True
                    print("There has been an overlap in the entered time, please try again")
                    st_time = input("Enter start time in 24hr format (00:00): ")
                    st_time = check_time_format(st_time)
                    end_time = input("Enter end time in 24hr format (00:00): ")
                    end_time = check_time_format(end_time)
                    break  

        if not overlap:
            break

    event = {
        'name': name,
        'date': date,
        'st_time': st_time,
        'end_time': end_time,
        'location': location,
        'description': description,
        'attendees': []
    }

    events[event_id] = event
    print(f"Event '{name}' added successfully.")


def print_schedule():
    if not events:
        print("\nNo events scheduled.")
        return

    print("\nEvents:")
    for event_id, event in events.items():
        print(f"[{event_id}] {event['name']}")

    while True:
        display_choice=input("Enter the event you would like to view the details of : ")
        if display_choice.isdigit():
            display_choice=int(display_choice)
            if display_choice<=len(events):
                break
            else:
                print("Event not found")
        else:
            print("Please type a numerical value")

    for event_id, event in events.items():
        if display_choice==event_id:
            print(f"\nEvent ID: {event_id}")
            print(f"Name: {event['name']}")
            print(f"Date: {event['date']}")
            print(f"Start Time: {event['st_time']}")
            print(f"End Time: {event['end_time']}")
            print(f"Location: {event['location']}")
            print(f"Description: {event['description']}")
            
            if event['attendees']:
                print("\nAttendees:")
                for i in range(len(event['attendees'])):
                    print(f"{i+1}. {event['attendees'][i]}")



def check_time_format(time):
    while True:
        parts = time.split(":")
        if len(parts) == 2 and all(part.isdigit() for part in parts):
            start_hour, start_minute = map(int, parts)
            if 0 <= start_hour <= 23 and 0 <= start_minute <= 59:
                if len(parts[1])<=2:
                    parts[0]=parts[0].lstrip("0")
                    time=f"{parts[0]}:{parts[1]}"
                    return time
        print("Wrong format or invalid time, please enter the time again (hh:mm)")
        time=input("Enter time again in 24hr format (00:00): ")


def time_convert(time):
    parts = time.split(":")
    start_hour, start_minute = map(int, parts)
    time_in_minutes=start_hour * 60 + start_minute
    return time_in_minutes

def check_overlap(event_start_time, event_end_time, new_start_time, new_end_time):
    if new_end_time<new_start_time:
        return True
    else:
        pass
    if (event_start_time < new_start_time < event_end_time) or \
        (event_start_time < new_end_time < event_end_time):
        return True
    else:
        if (new_start_time <= event_start_time):
            if (new_end_time <= event_start_time):
                return False
            else:
                return True

def check_date_format(date):
    while True:
        parts = date.split("/")
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            day, month, year = map(int, parts)
            if 1 <= day <= 31 and 1 <= month <= 12:
                for i in range(len(parts)):
                    parts[i]=parts[i].lstrip("0")
                date=f"{parts[0]}/{parts[1]}/{parts[2]}"
                print("Date entered:", date)
                return date
        print("Wrong format or invalid date, please try again")
        date = input("Enter the event date (DD/MM/YYYY) : ")


def delete_event():
    if not events:
        print("\nNo events to remove")
        return
    
    print("\nEvents:")
    for event_id, event in events.items():
        print(f"[{event_id}] {event['name']}")
    print(f"[{event_id+1}] Back to main menu")

    while True:
        remove_choice=input("Enter the event ID to be removed : ")
        if remove_choice.isdigit():
            remove_choice=int(remove_choice)
            if remove_choice == event_id+1:
                return
            if 0<remove_choice<=len(events):
                break
            else:
                print("Event not found")
        else:
            print("Please type a numerical value")

    if remove_choice in events:
        print(f"{events[remove_choice]['name']} deleted successfully.")
        del events[remove_choice]

def upd_events_dets():
    if not events:
        print("\nNo events to update")
        return
    
    print("\nEvents:")
    for event_id, event in events.items():
        print(f"[{event_id}] {event['name']}")

    while True:
        upd_choice=input("Enter the event ID to be updated : ")
        if upd_choice.isdigit():
            upd_choice=int(upd_choice)
            if 0<upd_choice<=len(events):
                break
            else:
                print("Event not found")
        else:
            print("Please type a numerical value")
    
    for event_id, event in events.items():
        if upd_choice==event_id:
            print(f"\nEvent ID: {event_id}")
            print(f"[1] Name: {event['name']}")
            print(f"[2] Date: {event['date']}")
            print(f"[3] Time:")
            print(f"Start Time: {event['st_time']}")
            print(f"End Time: {event['end_time']}")
            print(f"[4] Location: {event['location']}")
            print(f"[5] Description: {event['description']}")
            print(f"[6] Back to main menu")
                
        
    while True:
        upd_detail_choice=input("Enter the event detail ID to be updated : ")
            
        if upd_detail_choice == "1":
            for i in range(len(events)):
                if upd_choice==event_id:
                    new_e_name=input("Enter a new event name : ")
                    print(f"{events[event_id]['name']} successfully changed to {new_e_name}")
                    events[event_id]['name']=new_e_name
                    return
            
        elif upd_detail_choice == "2":
            while True:
                overlap=False
                new_date=input("Enter a new event date : ")
                new_date=check_date_format(new_date)
                for event_id, event in events.items():
                    if upd_choice==event_id:
                        for existing_event_id,existing_event in events.items():
                            if existing_event_id != upd_choice and existing_event['location'] == event['location'] and existing_event['date'] == new_date:
                                event_start_time = time_convert(existing_event['st_time'])
                                event_end_time = time_convert(existing_event['end_time'])
                                new_start_time = time_convert(event['st_time'])
                                new_end_time = time_convert(event['end_time'])
                                if check_overlap(event_start_time, event_end_time, new_start_time, new_end_time):
                                    overlap=True
                                    print("There is an overlap with an event on the same date")
                                    break
                if not overlap:
                    break
            events[event_id]['date']=new_date
            return

        elif upd_detail_choice == "3":
            while True:
                new_st_time = input("Enter a new start time in 24hr format (00:00): ")
                new_st_time = check_time_format(new_st_time)
                print("New start time entered:", new_st_time)
                new_end_time = input("Enter a new end time in 24hr format (00:00): ")
                new_end_time = check_time_format(new_end_time)
                new_st = time_convert(new_st_time)
                new_end = time_convert(new_end_time)
                if new_end <= new_st:
                    print("End time must be after start time")
                    pass
                else:
                    overlap = False
                    for event_id, event in events.items():
                        if upd_choice == event_id:
                            for existing_event_id, existing_event in events.items():
                                if existing_event_id != upd_choice and existing_event['location'] == event['location'] and existing_event['date'] == event['date']:
                                    event_start_time = time_convert(existing_event['st_time'])
                                    event_end_time = time_convert(existing_event['end_time'])
                                    if check_overlap(event_start_time, event_end_time, new_st, new_end):
                                        overlap = True
                                        print("There is an overlap with an event on the same date")
                                        break
                    if not overlap:
                        break
            events[event_id]['st_time']=new_st_time
            events[event_id]['end_time']=new_end_time
            return


        elif upd_detail_choice == "4":
            while True:
                overlap=False
                while True:
                    new_location=input("Enter event location: ").lstrip(" ")
                    if new_location=="":
                        print("empty space is not a location")
                    else:
                        break
                for event_id, event in events.items():
                    if upd_choice==event_id:
                        for existing_event_id, existing_event in events.items():
                            if existing_event_id != upd_choice and existing_event['location'] == new_location and existing_event['date'] == event['date']:
                                event_start_time = time_convert(existing_event['st_time'])
                                event_end_time = time_convert(existing_event['end_time'])
                                new_start_time = time_convert(event['st_time'])
                                new_end_time = time_convert(event['end_time'])
                                if check_overlap(event_start_time, event_end_time, new_start_time, new_end_time):
                                    overlap=True
                                    print("There is an overlap with an event on the same date")
                                    break
                if not overlap:
                    break
            events[event_id]['location']=new_location
            return

        elif upd_detail_choice == "5":
            while True:
                new_desc=input("Enter a new event description: ").lstrip(" ")
                if new_desc=="":
                    print("empty space is not a description")
                else:
                    break
            events[event_id]['description']=new_desc
            return

                
        elif upd_detail_choice == "6":
            print("going to main menu")
            return
        
        else:
            print('Invalid input. Try again.')
        

def upd_attendee_details():
    if not events:
        print("\nNo events to update")
        return
    
    print("\nEvents:")
    for event_id, event in events.items():
        print(f"[{event_id}] {event['name']}")

    while True:
        upd_attendee_choice=input("Enter the event ID to be updated : ")
        if upd_attendee_choice.isdigit():
            upd_attendee_choice=int(upd_attendee_choice)
            if 0<upd_attendee_choice<=len(events):
                break
            else:
                print("Event not found")
        else:
            print("Please type a numerical value")
    
    while True:
        print(f"\n\t\t\tevent: {events[event_id]['name']}")
        print("""           \n\t\t\tOptions:
                    [1] register attendees
                    [2] Remove attendees
                    [3] Update attendee's name
                    [4] Back to main menu
                        """)
        update_attendee=input("Enter the number corresponding to the function you would like to perform : ")
        
        if update_attendee == "1":
            while True:
                num_of_attendee=input("How many attendees would you like to register? : ")
                if num_of_attendee.isdigit():
                    num_of_attendee=int(num_of_attendee)
                    break
                else:
                    print("Please enter a numerical value")
            for i in range(num_of_attendee):
                while True:
                    new_attendee=input("Enter the name of the attendee to be registered : ").lstrip(" ")
                    if new_attendee == "":
                        print("Empty space is not a name")
                    else:
                        break
                events[event_id]['attendees'].append(new_attendee)
                print(f"Successfully added {new_attendee} to the event")

        elif update_attendee == "2":
            if events[event_id]['attendees']:
                for i in range(len(events[event_id]['attendees'])):
                    print(f"[{i+1}] {events[event_id]['attendees'][i]}")
                print(f"[{i+2}] Back to attendee menu")

                while True:
                    remove_attendee_choice=input("Index of attendee to be removed : ")
                    if remove_attendee_choice.isdigit():
                        remove_attendee_choice=int(remove_attendee_choice)
                        if 0<remove_attendee_choice<=i+2:
                            break
                        else:
                            print("Invalid choice, try again")
                    else:
                        print("Please enter a numerical value")
                if remove_attendee_choice == i+2:
                    pass
                else:
                    print(f"Successfully removed {events[event_id]['attendees'][remove_attendee_choice-1]} from the event")
                    events[event_id]['attendees'].pop(remove_attendee_choice-1)
            else:
                print("No attendees in event to remove")

        elif update_attendee == "3":
            if events[event_id]['attendees']:
                for i in range(len(events[event_id]['attendees'])):
                    print(f"[{i+1}] {events[event_id]['attendees'][i]}")
                print(f"[{i+2}] Back to attendee menu")

                while True:
                    attendee_choice=input("Index of attendee to be updated : ")
                    if attendee_choice.isdigit():
                        attendee_choice=int(attendee_choice)
                        if 0<attendee_choice<=i+2:
                            break
                        else:
                            print("Invalid choice, try again")
                    else:
                        print("Please enter a numerical value")

                while True:
                    if attendee_choice == i+2:
                        break
                    else:
                        new_attendee_name=input("Enter new attendee name : ").lstrip(" ")
                        if new_attendee_name == "":
                            print("Empty space is not a name")
                        else:
                            events[event_id]['attendees'][attendee_choice-1]=new_attendee_name
                            break
            else:
                print("No attendees in event to be updated")

        elif update_attendee == "4":
            return

        else:
            print("Invalid input, try again")






while True:
    print("""
          Event Manager
          [1] Add event
          [2] Remove event
          [3] Update event details
          [4] Update attendee details
          [5] Display event details
          [6] Quit
          """)
    
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            e_name=input("Enter event name: ").lstrip(" ")
            if e_name=="":
                print("empty space is not a name")
            else:
                break
        e_date=input("Enter event date (DD/MM/YYYY): ")
        e_date=check_date_format(e_date)
        while True:
            e_location=input("Enter event location: ").lstrip(" ")
            if e_location=="":
                print("empty space is not a location")
            else:
                break
        while True:
            e_description=input("Enter event description: ").lstrip(" ")
            if e_description=="":
                print("empty space is not a description")
            else:
                break
        while True:
            st_time=input("Enter start time in 24hr format (00:00): ")
            st_time=check_time_format(st_time)
            print("Start time entered:", st_time)
            end_time=input("Enter end time in 24hr format (00:00): ")
            end_time=check_time_format(end_time)
            st=time_convert(st_time)
            end=time_convert(end_time)
            if end<=st:
                print("End time must be after start time")
                pass
            else:
                print("End time entered:", end_time)
                break
        add_event(e_name, e_date, st_time, end_time, e_location, e_description)
    elif choice == "2":
        delete_event()
    elif choice == "3":
        upd_events_dets()
    elif choice == "4":
        upd_attendee_details()
    elif choice == "5":
        print_schedule()
    elif choice == "6":
        print("Thank you for using Event Manager.")
        break
    else:
        print("Invalid choice")
