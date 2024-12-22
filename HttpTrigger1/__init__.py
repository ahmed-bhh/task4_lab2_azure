import math
import azure.functions as func
import json


# Fonction pour effectuer l'intégration numérique
def numerical_integration(lower, upper, N):
    step = (upper - lower) / N
    total_area = 0.0
    for i in range(N):
        x = lower + i * step
        total_area += math.fabs(math.sin(x)) * step
    return total_area


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Azure Function HTTP trigger."""
    try:
        # Extraction des paramètres lower et upper depuis la requête
        lower = req.params.get("lower")
        upper = req.params.get("upper")

        if not lower or not upper:
            return func.HttpResponse(
                "Please provide both 'lower' and 'upper' query parameters.",
                status_code=400
            )

        lower = float(lower)
        upper = float(upper)
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid input. Please provide valid float numbers."}),
            status_code=400,
            mimetype="application/json"
        )

    N_values = [10, 50, 100, 1000, 10000, 100000, 1000000]  # Différentes valeurs de N
    results = []

    for N in N_values:
        result = numerical_integration(lower, upper, N)
        results.append({"N": N, "Result": result})

    # Renvoi de la réponse en JSON
    return func.HttpResponse(
        json.dumps(results),
        status_code=200,
        mimetype="application/json"
    )

#http://localhost:7071/api/HttpTrigger1?lower=0&upper=3.14159
 
 #https://task4lab2ahmed.azurewebsites.net/api/httptrigger1?code=_IGT90Qq4AbQLXjUQV211qKAAI2kS4KCTwcfqP5vK-JXAzFuKJN6dQ%3D%3D&lower=0&upper=3.14159