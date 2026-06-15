class DiagnosisAgent:

    def validate_distance(
        self,
        measured_distance,
        reference_distance,
        tolerance
    ):

        error = abs(
            measured_distance -
            reference_distance
        )

        if error <= tolerance:

            status = "CORRECTA"

            explanation = (
                "La distancia está dentro "
                "de la tolerancia permitida."
            )

        else:

            status = "INCORRECTA"

            explanation = (
                "La distancia excede "
                "la tolerancia permitida."
            )

        return {
            "status": status,
            "error": round(error, 3),
            "explanation": explanation
        }