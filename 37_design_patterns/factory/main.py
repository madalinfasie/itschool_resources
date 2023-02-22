import abc
import typing as t


class MijlocTransport(abc.ABC):
    @abc.abstractmethod
    def transport(self, marfa: t.Any, ruta: str):
        pass


class Transport(abc.ABC):
    @abc.abstractmethod
    def planificare_ruta(self, sursa: str, destinatie: str) -> str:
        pass

    @abc.abstractmethod
    def creare_transport(self) -> MijlocTransport:
        pass


class Tir(MijlocTransport):
    def transport(self, marfa: t.Any, ruta: str):
        print(f'Transport cu tirul {marfa} pe ruta {ruta}')


class Vapor(MijlocTransport):
    def transport(self, marfa: t.Any, ruta: str):
        print(f'Transport cu vaporul {marfa} pe ruta {ruta}')


class TransportRutier(Transport):
    def planificare_ruta(self, sursa: str, destinatie: str) -> str:
        return f'Plec din {sursa} si ajung in {destinatie}'

    def creare_transport(self) -> MijlocTransport:
        return Tir()


class TransportNautic(Transport):
    def planificare_ruta(self, sursa: str, destinatie: str) -> str:
        return f'Plec din {sursa} si ajung in {destinatie}'

    def creare_transport(self) -> MijlocTransport:
        return Vapor()


class Depozit:
    def procesare_comanda(self, comanda: t.List[dict]):
        for obiect in comanda:
            if obiect['tip'] == 'vapor':
                factory = TransportNautic()
            elif obiect['tip'] == 'rutier':
                factory = TransportRutier()
            else:
                raise Exception('nu e un transport valid')

            ruta = factory.planificare_ruta(
                sursa=obiect['sursa'],
                destinatie=obiect['destinatie'])

            mijloc_transport = factory.creare_transport()
            mijloc_transport.transport(obiect['marfa'], ruta)


if __name__ == '__main__':
    comanda = [
        {
            'tip': 'vapor',
            'sursa': 'turcia',
            'destinatie': 'constanta',
            'marfa': ['baclava', 'bluze']
        },
        {
            'tip': 'rutier',
            'sursa': 'bucuresti',
            'destinatie': 'budapesta',
            'marfa': ['oi', 'autonomie']
        }
    ]

    app = Depozit()
    app.procesare_comanda(comanda)


