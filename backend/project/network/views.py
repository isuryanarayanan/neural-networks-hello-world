"""
This file contains the views for the network app.
"""

# Native imports
import json

# Django imports
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Graphene imports
from network.schema.schema import schema

# Local imports
from utils.views import GraphQLRespondView


@csrf_exempt
def network_graphql_view(request):
    # Use extended view
    return GraphQLRespondView.as_view(graphiql=True, schema=schema)(request)
