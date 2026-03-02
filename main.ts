let luminosidade = 0
let temperatura = 0
datalogger.setColumnTitles(
"temperaratura",
"luminosidade"
)
loops.everyInterval(1000, function () {
    temperatura = pins.analogReadPin(AnalogPin.P0)
    luminosidade = pins.analogReadPin(AnalogReadWritePin.P1)
    datalogger.log(
    datalogger.createCV("temperaratura", temperatura),
    datalogger.createCV("luminosidade", luminosidade)
    )
})
