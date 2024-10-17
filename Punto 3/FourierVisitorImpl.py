from FourierParserVisitor import FourierParserVisitor  # Importar la clase generada por ANTLR
import numpy as np
from math import pi, e, sin, cos

class FourierVisitorImpl(FourierParserVisitor):

    def visitFourierTransform(self, ctx):
        # Obtener la lista de secuencias
        sequence = self.visit(ctx.list_())
        # Realizar la Transformada de Fourier
        result = np.fft.fft(sequence)
        print(f"Transformada de Fourier: {result}")
        return result

    def visitInverseTransform(self, ctx):
        # Obtener la lista de secuencias
        sequence = self.visit(ctx.list_())
        # Realizar la Transformada Inversa
        result = np.fft.ifft(sequence)
        print(f"Transformada Inversa: {result}")
        return result

    def visitTransformPair(self, ctx):
        # Obtener el número de frecuencia
        frequency = int(ctx.NUMBER().getText())
        transform_pairs = {1: "pair1", 2: "pair2"}
        print(f"Pares transformados para la frecuencia {frequency}: {transform_pairs.get(frequency, 'No encontrado')}")
        return transform_pairs.get(frequency, None)

    def visitList(self, ctx):
        # Procesar la lista de números o expresiones
        elements = [self.visit(e) for e in ctx.expr()]
        return elements

    # Operaciones aritméticas
    def visitAddition(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitSubtraction(self, ctx):
        return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))

    def visitMultiplication(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitDivision(self, ctx):
        return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))

    # Manejo de constantes Pi y Euler
    def visitPiConstant(self, ctx):
        return pi

    def visitEulerConstant(self, ctx):
        return e

    # Funciones trigonométricas
    def visitSinFunction(self, ctx):
        return np.sin(self.visit(ctx.expr()))

    def visitCosFunction(self, ctx):
        return np.cos(self.visit(ctx.expr()))
        
    def visitNumber(self, ctx):
        return float(ctx.NUMBER().getText())

    def visitParentheses(self, ctx):
        return self.visit(ctx.expr())

