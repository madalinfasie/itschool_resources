import abc
import typing as t


class MijlocTransport(abc.ABC):
    @abc.abstractmethod
    def transporta(self, marfa: t.Any, ruta: t.Any):
        pass


class Transport(abc.ABC):
    @abc.abstractmethod
    def planificare_ruta(self, sursa: str, destinatie: str):
        pass

    @abc.abstractmethod
    def creare_transport(self) -> MijlocTransport:
        pass


class Tir(MijlocTransport):
    def transporta(self, marfa: t.Any, ruta: t.Any):
        print(f'Transport cu tirul {marfa} pe ruta {ruta}')


class Vapor(MijlocTransport):
    def transporta(self, marfa: t.Any, ruta: t.Any):
        print(f'Transport cu vaporul {marfa} pe ruta {ruta}')


class TransportRutier(Transport):
    def planificare_ruta(self, sursa: str, destinatie: str):
        return f'pleaca din {sursa} o ia pe la braila si se intoarce pe pitesti pana la {destinatie}'

    def creare_transport(self) -> MijlocTransport:
        return Tir()


class TransportNautic(Transport):
    def planificare_ruta(self, sursa: str, destinatie: str):
        return f'merge pe marea neagra de la {sursa} pana in {destinatie}'

    def creare_transport(self) -> MijlocTransport:
        return Vapor()


class Depozit:
    def procesare_comanda(self, comanda):
        for obiect in comanda:
            if obiect['tip'] == 'vapor':
                transport_factory = TransportNautic()
            else:
                transport_factory = TransportRutier()

            mijloc_transport = transport_factory.creare_transport()
            ruta = transport_factory.planificare_ruta(obiect['sursa'], obiect['destinatie'])

            mijloc_transport.transporta(obiect['marfa'], ruta)


if __name__ == '__main__':
    comanda = [
        {
            'sursa': 'Bucuresti',
            'destinatie': 'Cluj',
            'tip': 'rutier',
            'marfa': ['oi', 'capre', 'papagali']
        },
        {
            'sursa': 'Turcia',
            'destinatie': 'Constanta',
            'tip': 'vapor',
            'marfa': ['baclava', 'camasi']
        }
    ]

    depozit = Depozit()
    depozit.procesare_comanda(comanda)