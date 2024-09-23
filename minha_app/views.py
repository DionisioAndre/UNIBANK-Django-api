from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model 



@api_view(["GET"])
def get_bancos(request):
    try:
        bancos = Banco.objects.all()
        serializer = BancoSerializer(bancos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def get_contas(request):
    try:
        bancos = Conta.objects.all()
        serializer = ContaSerializer(bancos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_perfis(request):
    try:
        bancos = Perfil.objects.all()
        serializer = PerfilSerializer(bancos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def deletarBanco(request, banco_id):
    try:
        banco = Banco.objects.get(id=banco_id)
        banco.delete()
        return Response({"data": "sucesso"}, status=status.HTTP_200_OK)
    except Banco.DoesNotExist as e:
        print(e)
        return Response({"data": "banco não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def deletarConta(request, conta_id):
    try:
        conta = Conta.objects.get(id=conta_id)
        conta.delete()
        return Response({"data": "sucesso"}, status=status.HTTP_200_OK)
    except Conta.DoesNotExist as e:
        print(e)
        return Response({"data": "Conta não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BancoByNameView(APIView):
    def get(self, request, name):
        try:
            banco = Banco.objects.get(banco=name)
        except Banco.DoesNotExist:
            return Response({"error": "Banco não encontrado"},status=status.HTTP_404_NOT_FOUND)
        serializer = BancoSerializer(banco)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BancoById(APIView):
    def get(self, request, pk):
        try:
            banco = Banco.objects.get(id=pk)
        except Banco.DoesNotExist:
            return Response({"error": "Banco não encontrado"},status=status.HTTP_404_NOT_FOUND)
        serializer = BancoSerializer(banco)
        return Response(serializer.data, status=status.HTTP_200_OK)
class ContaById(APIView):
    def get(self, request, pk):
        try:
            conta = Conta.objects.get(id=pk)
        except Conta.DoesNotExist:
            return Response({"error": "conta não encontrado"},status=status.HTTP_404_NOT_FOUND)
        serializer = ContaSerializer(conta)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def put(request,pk):    
    try:
        banco = Banco.objects.get(pk=pk)
    except Banco.DoesNotExist:
        return Response({"error": "Banco não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    serializer = BancoSerializer(banco, data=request.data, partial=True)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def criarBancos(request):
    if request.method=='POST':
        serializer=BancoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def criarConta(request):
    if request.method=='POST':
        serializer=ContaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def criarBanacos2(request):
    try:
        data=request.data
        funcionario=User.objects.get(funcionarioId=data['funcionarioId'])
        Banco.objects.create(
            banco=data['banco'],
            id=funcionario, )
        return Response({"data":"sucesso"}, status=status.HTTP_200_OK)
    except funcionario.DoesNotExist as e:
        print(e)
        return Response({"data":"bad user id"},status= status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)