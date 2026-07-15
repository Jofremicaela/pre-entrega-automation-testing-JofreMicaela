from behave import given,when,then
import requests


headers = {
    "x-api-key": "pub_afa259568dd51a623ad1d66dbdd696c7d70b9a0bb385430e21eb2e036aae9534"
}

@given("la API a Reqres esta disponible")
def step_impl(context):
    context.base_url= "https://reqres.in/api"
    
@when("realizar un login valido")
def step_impl(context):
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    
    context.response = requests.post(
                        f"{context.base_url}/login",
                        headers=headers,
                        json = body 
    )
    
@then("el status code debe ser {status_code:d}")
def step_impl(context,status_code):
    print(f"status{context.response.status_code}")
    assert context.response.status_code == status_code
    
##Scenario2

@when("realizar un login sin contraseña")
def step_impl(context):
    body = {
        "email": "eve.holt@reqres.in",
    }
    context.response = requests.post(
                        f"{context.base_url}/login",
                        headers=headers,
                        json = body 
    )
@then("el mensaje de error debe ser '{mensaje}'")
def step_impl(context,mensaje):
    body = context.response.json()
    
        
    assert body["error"] == mensaje