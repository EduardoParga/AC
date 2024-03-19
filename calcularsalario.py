def calcula_salario(valor_hora, num_horas, irpf):
    irpf == 0.275
    bruto = valor_hora * num_horas
    salario_liquido = bruto - bruto * irpf
    return salario_liquido