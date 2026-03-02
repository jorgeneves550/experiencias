luminosidade = 0
temperatura = 0
datalogger.set_column_titles("temperaratura", "luminosidade")

def on_every_interval():
    global temperatura, luminosidade
    temperatura = pins.analog_read_pin(AnalogPin.P0)
    luminosidade = pins.analog_read_pin(AnalogReadWritePin.P1)
    datalogger.log(datalogger.create_cv("temperaratura", temperatura),
        datalogger.create_cv("luminosidade", luminosidade))
loops.every_interval(1000, on_every_interval)
