from abc import ABC, abstractmethod

class NutritionPlan:
    def __init__(self):
        self.caloric_intake = 0
        self.macronutrient_ratios = {"carbohydrates": 0, "proteins": 0, "fats": 0}
        self.meal_plans = []
        self.fitness_goal = ""
        self.dietary_restrictions = []

    def __str__(self):
        return f"Nutrition Plan:\nCaloric Intake: {self.caloric_intake}\nMacronutrient Ratios: {self.macronutrient_ratios}\nMeal Plans: {self.meal_plans}\nFitness Goal: {self.fitness_goal}\nDietary Restrictions: {self.dietary_restrictions}"

class NutritionPlanBuilder(ABC):
    @abstractmethod
    def set_caloric_intake(self, caloric_intake):
        pass

    @abstractmethod
    def set_macronutrient_ratios(self, carbohydrates, proteins, fats):
        pass

    @abstractmethod
    def set_meal_plans(self, meal_plans):
        pass

    @abstractmethod
    def set_fitness_goal(self, fitness_goal):
        pass

    @abstractmethod
    def set_dietary_restrictions(self, dietary_restrictions):
        pass

    @abstractmethod
    def build(self):
        pass

class NutritionPlanDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def create_nutrition_plan(self):
        self.builder.set_caloric_intake(2000)
        self.builder.set_macronutrient_ratios(40, 30, 30)
        self.builder.set_meal_plans(["Breakfast: Eggs and Avocado", "Lunch: Grilled Chicken Salad", "Dinner: Salmon with Quinoa"])
        self.builder.set_fitness_goal("Weight Loss")
        self.builder.set_dietary_restrictions(["Gluten-free", "Lactose-free"])
        return self.builder.build()

class WeightLossNutritionPlanBuilder(NutritionPlanBuilder):
    def __init__(self):
        self.nutrition_plan = NutritionPlan()

    def set_caloric_intake(self, caloric_intake):
        self.nutrition_plan.caloric_intake = caloric_intake

    def set_macronutrient_ratios(self, carbohydrates, proteins, fats):
        self.nutrition_plan.macronutrient_ratios = {"carbohydrates": carbohydrates, "proteins": proteins, "fats": fats}

    def set_meal_plans(self, meal_plans):
        self.nutrition_plan.meal_plans = meal_plans

    def set_fitness_goal(self, fitness_goal):
        self.nutrition_plan.fitness_goal = fitness_goal

    def set_dietary_restrictions(self, dietary_restrictions):
        self.nutrition_plan.dietary_restrictions = dietary_restrictions

    def build(self):
        return self.nutrition_plan

# Usage example
director = NutritionPlanDirector()
builder = WeightLossNutritionPlanBuilder()
director.set_builder(builder)
nutrition_plan = director.create_nutrition_plan()
print(nutrition_plan)

import copy

class Maze:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_no] = room

    def room_no(self, room_no):
        return self.rooms.get(room_no)

class Direction:
    NORTH = "North"
    EAST = "East"
    SOUTH = "South"
    WEST = "West"

class Room:
    def __init__(self, room_no):
        self.sides = {}
        self.room_no = room_no

    def get_side(self, direction):
        return self.sides.get(direction)

    def set_side(self, direction, wall):
        self.sides[direction] = wall

class Wall:
    pass

class DoorWall(Wall):
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
        self.is_open = False

def clone_maze(maze):
    return copy.deepcopy(maze)

# Usage example
maze = Maze()
r1 = Room(1)
r2 = Room(2)
d = DoorWall(r1, r2)

maze.add_room(r1)
maze.add_room(r2)

r1.set_side(Direction.NORTH, d)
r1.set_side(Direction.EAST, Wall())
r1.set_side(Direction.SOUTH, Wall())
r1.set_side(Direction.WEST, Wall())
r2.set_side(Direction.NORTH, Wall())
r2.set_side(Direction.EAST, Wall())
r2.set_side(Direction.SOUTH, d)
r2.set_side(Direction.WEST, Wall())

cloned_maze = clone_maze(maze)
print("Cloned Maze Rooms:", list(cloned_maze.rooms.keys()))
