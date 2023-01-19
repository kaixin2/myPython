

# error3
#  1  def init(self, name, health_points):
#  2   self.health_points -= pt
#  3   > -> >=



class Person:
    # Error 1
    def __init__(self, name, health_points):
        self.name = name
        self.health_points = health_points

    def award_health_points(self, pt):
        # Error 2
        self.health_points += pt
        return self.health_points


def add_health_points(name, health_points, steps):
    person1 = Person(name, health_points)

    # Error 3
    if steps >= 10000:
        return person1.award_health_points(40)
    elif steps >= 7500:
        return person1.award_health_points(25)
    elif steps >= 5000:
        return person1.award_health_points(10)
    else:
        return person1.award_health_points(0)