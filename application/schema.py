import graphene
from restaurant.schema import RestaurantQuery, RestaraurantMutation

class Query(RestaurantQuery, graphene.ObjectType):
    pass

class Mutation(RestaraurantMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
