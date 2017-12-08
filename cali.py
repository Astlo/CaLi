import argparse
import utils.LicensesPowersetGenerator as PowersetGenerator
from lattice.LicensesLattice import LicensesLattice
import utils.PlotlyLattice as Plotly


def main():
    parser = argparse.ArgumentParser(prog='cali', description='Experiments with lattice.')
    parser.add_argument('filename', metavar='f', type=str, nargs='+',
                        help='json file containing terms')
    args = parser.parse_args()
    terms = ['a', 'b']
    powerset = PowersetGenerator.generate_licenses(terms)
    cali = LicensesLattice(terms, powerset)
    cali.generate_lattice()
    Plotly.draw(cali, 0.1, 0.1)


if __name__ == "__main__":
    main()