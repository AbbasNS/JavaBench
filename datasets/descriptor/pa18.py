project = {
    "todo_root": "./projects/PA18/src/main/java/",
    "context_root": "./projects/PA18-Context/src/main/java/",
    "requirements": "./projects/PA18/readme.md",
    "tasks": {
        "Game.java": {
            "target": "Game.java",
            "related_source_list": [
                "Exceptions/InvalidMapException.java",
                "Map/Cell.java",
                "Map/Wall.java",
                "Map/Map.java",
                "Map/Occupant/Crate.java",
                "Map/Occupiable/DestTile.java",
            ],
        },
        "Map.java": {
            "target": "Map/Map.java",
            "related_source_list": [
                "Exceptions/InvalidMapException.java",
                "Exceptions/InvalidNumberOfPlayersException.java",
                "Exceptions/UnknownElementException.java",
                "Map/Cell.java",
                "Map/Occupant/Crate.java",
                "Map/Occupant/Player.java",
                "Map/Occupiable/DestTile.java",
                "Map/Occupiable/Occupiable.java",
                "Map/Occupiable/Tile.java",
                "Map/Wall.java",
            ],
        },
        "Tile.java": {
            "target": "Map/Occupiable/Tile.java",
            "related_source_list": [
                "Map/Occupiable/Occupiable.java",
                "Map/Occupant/Occupant.java",
                "Map/Cell.java",
            ],
        },
        "DestTile.java": {
            "target": "Map/Occupiable/DestTile.java",
            "related_source_list": [
                "Map/Occupiable/Tile.java",
                "Map/Occupant/Occupant.java",
                "Map/Occupant/Crate.java",
            ],
        },
    },
}
