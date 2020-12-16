class BancoDeDados(object):
    def __init__(self):
        # DABEL, DAENT, DAGUA, DABEN, DASAC
        self.bairros = {
            'Batista Campos' : {'coordenadas':(-1.4605943431379507, -48.489817446635655), 'centroide': None},
            'Campina' : {'coordenadas':(-1.451566195417784, -48.49904909461015), 'centroide': None},
            'Cidade Velha' : {'coordenadas':(-1.4608155705226513, -48.50614211759469), 'centroide': None},
            'Fatima' : {'coordenadas':(-1.4416052744484091, -48.47249206212274), 'centroide': None},
            'Nazare' : {'coordenadas':(-1.4539594926806354, -48.48123052840319), 'centroide': None},
            'Reduto' : {'coordenadas':(-1.445978774760613, -48.49249213076001), 'centroide': None},
            'Sao Bras' : {'coordenadas':(-1.4515463874839785, -48.47080274126891), 'centroide': None},
            'Umarizal' : {'coordenadas':(-1.4414126980100477, -48.48375311397722), 'centroide': None},
            'Marco' : {'coordenadas':(-1.4352675908435437, -48.46126363796704), 'centroide': None},
            
            'Curio-Utinga' : {'coordenadas':(-1.430480180009479, -48.446548277162066), 'centroide': None},
            'Aguas Lindas' : {'coordenadas':(-1.4055723052634344, -48.39512702712799), 'centroide': None},
            'Aura' : {'coordenadas':(-1.4082851671255567, -48.39753461893008), 'centroide': None},
            'Castanheira' : {'coordenadas':(-1.4086947376898031, -48.43140820637047), 'centroide': None},
            'Guanabara' : {'coordenadas':(-1.398005, -48.414907), 'centroide': None},
            'Mangueirao' : {'coordenadas':(-1.3782816029283569, -48.44530337949438), 'centroide': None},
            'Marambaia' : {'coordenadas':(-1.4041742008591003, -48.453870278548415), 'centroide': None},
            'Souza' : {'coordenadas':(-1.414227808018852, -48.45288043857192), 'centroide': None},
            'Val-de-Cans' : {'coordenadas':(-1.3900919728908587, -48.47343004944939), 'centroide': None},
            
            'Canudos' : {'coordenadas':(-1.4535963272004575, -48.46126652913588), 'centroide': None},
            'Condor' : {'coordenadas':(-1.4722717460874073, -48.48125447066777), 'centroide': None},
            'Cremacao' : {'coordenadas':(-1.4613507708896258, -48.476347018758965), 'centroide': None},
            'Guamá' : {'coordenadas':(-1.4639542261610194, -48.463309854794716), 'centroide': None},
            'Jurunas' : {'coordenadas':(-1.4706879550670389, -48.4937855558099), 'centroide': None},
            'Terra Firme' : {'coordenadas':(-1.4571413558852695, -48.451256552002036), 'centroide': None},
            'Universitario' : {'coordenadas':(-1.4642624071829904, -48.44144549753805), 'centroide': None},
            
            'Bengui' : {'coordenadas':(-1.3752277654519802, -48.45536926945969), 'centroide': None},
            'Cabanagem' : {'coordenadas':(-1.3680783967719699, -48.43253656597374), 'centroide': None},
            'Coqueiro' : {'coordenadas':(-1.3380198721152354, -48.444047592715116), 'centroide': None},
            'Parque Verde' : {'coordenadas':(-1.367196806649681, -48.443823561243), 'centroide': None},
            'Pratinha' : {'coordenadas':(-1.3606098903250072, -48.47366357072046), 'centroide': None},
            'Sao Clemente' : {'coordenadas':(-1.3658988373419185, -48.461233164926185), 'centroide': None},
            'Tapana' : {'coordenadas':(-1.3386561496417695, -48.47389957731982), 'centroide': None},
            'Tenone' : {'coordenadas':(-1.318846552382267, -48.44106489733067), 'centroide': None},
            'Una' : {'coordenadas':(-1.3716708157278321, -48.42512094369472), 'centroide': None},
            
            'Barreiro' : {'coordenadas':(-1.4139701697170366, -48.484403616862224), 'centroide': None},
            'Maracangalha' : {'coordenadas':(-1.399284122891722, -48.48127950425518), 'centroide': None},
            'Miramar' : {'coordenadas':(-1.4067413308704868, -48.49130764971447), 'centroide': None},
            'Pedreira' : {'coordenadas':(-1.4245104972103562, -48.47122244428872), 'centroide': None},
            'Sacramenta' : {'coordenadas':(-1.4138489639930902, -48.476198120925744), 'centroide': None},
            'Telegrafo' : {'coordenadas':(-1.4260575726545308, -48.48733732870352), 'centroide': None},
        }