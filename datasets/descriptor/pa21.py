project = {
    "todo_root": "./projects/PA21/src/main/java/",
    "context_root": "./projects/PA21-Context/src/main/java/",
    "requirements": "./projects/PA21/README.md",
    "tasks": {
        "GameBoardController.java": {
            "target": "pa1/controller/GameBoardController.java",
            "related_source_list": [
                "pa1/model/Cell.java",
                "pa1/model/Direction.java",
                "pa1/model/Entity.java",
                "pa1/model/EntityCell.java",
                "pa1/model/ExtraLife.java",
                "pa1/model/GameBoard.java",
                "pa1/model/Gem.java",
                "pa1/model/Mine.java",
                "pa1/model/MoveResult.java",
                "pa1/model/Player.java",
                "pa1/model/Position.java",
                "pa1/model/PositionOffset.java",
                "pa1/model/StopCell.java",
            ],
        },
        "GameController.java": {
            "target": "pa1/controller/GameController.java",
            "related_source_list": [
                "pa1/controller/GameBoardController.java",
                "pa1/model/Direction.java",
                "pa1/model/GameState.java",
                "pa1/model/MoveResult.java",
                "pa1/model/MoveStack.java",
            ],
        },
        "Entity.java": {
            "target": "pa1/model/Entity.java",
            "related_source_list": [
                "pa1/model/BoardElement.java",
                "pa1/model/EntityCell.java",
                "pa1/model/ExtraLife.java",
                "pa1/model/Gem.java",
                "pa1/model/Mine.java",
                "pa1/model/Player.java",
            ],
        },
        "EntityCell.java": {
            "target": "pa1/model/EntityCell.java",
            "related_source_list": [
                "pa1/model/Cell.java",
                "pa1/model/Entity.java",
                "pa1/model/Position.java",
                "pa1/model/StopCell.java",
            ],
        },
        "ExtraLife.java": {
            "target": "pa1/model/ExtraLife.java",
            "related_source_list": [
                "pa1/model/Entity.java",
                "pa1/model/EntityCell.java",
            ],
        },
        "GameBoard.java": {
            "target": "pa1/model/GameBoard.java",
            "related_source_list": [
                "pa1/model/Cell.java",
                "pa1/model/Direction.java",
                "pa1/model/Entity.java",
                "pa1/model/EntityCell.java",
                "pa1/model/Gem.java",
                "pa1/model/Player.java",
                "pa1/model/Position.java",
                "pa1/model/PositionOffset.java",
                "pa1/model/StopCell.java",
                "pa1/model/Wall.java",
            ],
        },
        "GameState.java": {
            "target": "pa1/model/GameState.java",
            "related_source_list": [
                "pa1/controller/GameBoardController.java",
                "pa1/view/GameBoardView.java",
                "pa1/model/GameBoard.java",
                "pa1/model/MoveStack.java",
            ],
        },
        "Gem.java": {
            "target": "pa1/model/Gem.java",
            "related_source_list": [
                "pa1/model/Entity.java",
                "pa1/model/EntityCell.java",
            ],
        },
        "Mine.java": {
            "target": "pa1/model/Mine.java",
            "related_source_list": [
                "pa1/model/Entity.java",
                "pa1/model/EntityCell.java",
            ],
        },
        "MoveResult.java": {
            "target": "pa1/model/MoveResult.java",
            "related_source_list": [
                "pa1/model/Position.java",
                "pa1/model/ExtraLife.java",
                "pa1/model/Gem.java",
                "pa1/model/Mine.java",
            ],
        },
        "MoveStack.java": {
            "target": "pa1/model/MoveStack.java",
            "related_source_list": [
                "pa1/model/MoveResult.java",
            ],
        },
        "Player.java": {
            "target": "pa1/model/Player.java",
            "related_source_list": [
                "pa1/model/Entity.java",
                "pa1/model/EntityCell.java",
            ],
        },
        "Position.java": {
            "target": "pa1/model/Position.java",
            "related_source_list": [
                "pa1/model/PositionOffset.java",
            ],
        },
        "StopCell.java": {
            "target": "pa1/model/StopCell.java",
            "related_source_list": [
                "pa1/model/Entity.java",
                "pa1/model/EntityCell.java",
                "pa1/model/Player.java",
                "pa1/model/Position.java",
            ],
        }
    },
}
