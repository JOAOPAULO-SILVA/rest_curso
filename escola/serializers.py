from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, cel_num_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','cpf','nome','email', 'data_nasc','cel_num']

    def validate(self, attrs):
        if cpf_invalido(attrs["cpf"]):
            raise serializers.ValidationError({"cpf":"O CPF dever ter 11 digitos"})
        if nome_invalido(attrs["nome"]):
            raise serializers.ValidationError({"nome":"O nome só deve conter letras"})
        if cel_num_invalido(attrs["cel_num"]):
            raise serializers.ValidationError({"cel_num":"O numero deve seguir o padrão '99 99999-9999'"})
        return attrs
    
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudantesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = "curso.  descricao")
    turno = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ["curso", "turno"]
    def get_turno(self, obj):
        return obj.get_turno_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = "estudante.nome")
    class Meta:
        model = Matricula
        fields = ["estudante_nome"]

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email', 'cel_num']

    def validate(self, attrs):
        if cpf_invalido(attrs["cpf"]):
            raise serializers.ValidationError({"cpf":"O CPF dever ter 11 digitos"})
        if nome_invalido(attrs["nome"]):
            raise serializers.ValidationError({"nome":"O nome só deve conter letras"})
        if cel_num_invalido(attrs["cel_num"]):
            raise serializers.ValidationError({"cel_num":"O numero deve seguir o padrão '99 99999-9999'"})
        return attrs
    