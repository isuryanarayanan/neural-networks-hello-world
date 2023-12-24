"""
Schema for the network app
"""

# Graphene imports
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description="A simple greeting")

    def resolve_hello(self, info):
        return "Hello, world!"

schema = graphene.Schema(
    query=Query,
)
