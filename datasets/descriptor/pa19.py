project = {
    "todo_root": "./projects/PA19/src/main/java/",
    "context_root": "./projects/PA19-Context/src/main/java/",
    "requirements": "./projects/PA19/README.md",
    "tasks": {
        "Cell.java": {
            "target": "game/map/cells/Cell.java",
            "related_source_list": [
                "game/MapElement.java",
                "game/map/cells/FillableCell.java",
                "game/map/cells/TerminationCell.java",
                "game/map/cells/Wall.java",
                "util/Coordinate.java",
                "util/Direction.java",
            ],
        },
        "FillableCell.java": {
            "target": "game/map/cells/FillableCell.java",
            "related_source_list": [
                "game/MapElement.java",
                "game/map/cells/Cell.java",
                "game/pipes/Pipe.java",
                "util/Coordinate.java",
            ],
        },
        "TerminationCell.java": {
            "target": "game/map/cells/TerminationCell.java",
            "related_source_list": [
                "game/map/cells/Cell.java",
                "util/Coordinate.java",
                "util/Direction.java",
                "util/PipePatterns.java",
            ],
        },
        "Wall.java": {
            "target": "game/map/cells/Wall.java",
            "related_source_list": [
                "game/map/cells/Cell.java",
                "util/Coordinate.java",
                "util/PipePatterns.java",
            ],
        },
        "Map.java": {
            "target": "game/map/Map.java",
            "related_source_list": [
                "game/map/cells/Cell.java",
                "game/map/cells/FillableCell.java",
                "game/map/cells/TerminationCell.java",
                "game/map/cells/Wall.java",
                "game/pipes/Pipe.java",
                "io/Deserializer.java",
                "util/Coordinate.java",
                "util/Direction.java",
                "util/StringUtils.java",
            ],
        },
        "Pipe.java": {
            "target": "game/pipes/Pipe.java",
            "related_source_list": [
                "game/MapElement.java",
                "util/Direction.java",
                "util/PipePatterns.java",
            ],
        },
        "CellStack.java": {
            "target": "game/CellStack.java",
            "related_source_list": ["game/map/cells/FillableCell.java"],
        },
        "DelayBar.java": {
            "target": "game/DelayBar.java",
            "related_source_list": ["util/StringUtils.java"],
        },
        "Game.java": {
            "target": "game/Game.java",
            "related_source_list": [
                "game/map/cells/Cell.java",
                "game/map/cells/FillableCell.java",
                "game/pipes/Pipe.java",
                "io/Deserializer.java",
                "util/Coordinate.java",
                "game/map/Map.java",
                # Extra
                "game/DelayBar.java",
                "game/CellStack.java",
                "game/PipeQueue.java",
            ],
        },
        "PipeQueue.java": {
            "target": "game/PipeQueue.java",
            "related_source_list": [
                "game/pipes/Pipe.java",
            ],
        },
    },
}
