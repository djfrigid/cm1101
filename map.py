room_Reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics Reception. The Receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"south": "Admins" , "east" : "Tutor", "west": "Parking"}
}

room_admins = {
    "name": "MJ and Simon's room",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the Reception.""",

    "exits" : {"north" : "Reception"}
}

room_Tutor = {
    "name": "your personal Tutor's Office",

    "description":
    """You are in your personal Tutor's Office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The Reception is to the west.""",

    "exits" : {"west" : "Reception"}
}

room_Parking = {
    "name": "the Parking lot",

    "description":
    """You are standing in the Queen's Buildings Parking lot.
You can go south to the COMSC Reception, or east to the
general Office.""",

    "exits": {"south" : "Reception" , "east" : "Office"}
}

room_Office = {
    "name": "the general Office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits" : {"west" : "Parking"}
}



rooms = {
    "Reception": room_Reception,
    "Admins": room_admins,
    "Tutor": room_Tutor,
    "Parking": room_Parking,
    "Office": room_Office
}
