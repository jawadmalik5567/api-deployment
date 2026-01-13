from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AddNumbersAPIView(APIView):

    def post(self, request):
        try:
            num1 = request.data.get('num1')
            num2 = request.data.get('num2')

            if num1 is None or num2 is None:
                return Response(
                    {"error": "num1 and num2 are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            num1 = float(num1)
            num2 = float(num2)

            result = num1 + num2

            return Response(
                {
                    "num1": num1,
                    "num2": num2,
                    "addition": result,
                    "status": "success"
                },
                status=status.HTTP_200_OK
            )

        except ValueError:
            return Response(
                {"error": "num1 and num2 must be numbers"},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
