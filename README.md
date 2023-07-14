# E2 Alberto Domenic Rincon Espinoza
# Pregunta 3
Para solo limitar el la cantidad que se puede transferir por día se podría agregar un metodo nuevo a la clase cuenta con un flag el cual indique si ya sobrepasó el límite o no, este flag se seteara en falso (no llego al limite) al llegar las 00:00:00 . Para setear este flag durante el dia es nesesario realizar una modificación al metodo de la clase Cuenta pagar(dest, val), la modificación simplemente acumula un valor numerico a lo largo del día y si este llega  200 soles el flag se setea en True(ya alcanzó el límite).





