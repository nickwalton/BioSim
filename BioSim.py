from betse.metaapp import BetseMetaApp
from betse.cli.climain import BetseCLI
import yaml
import csv


def run_exp(yml_file):

    BetseMetaApp()

    # Seed the Simulator
    BetseCLI().run(["seed", yml_file])

    # Init the Simulator
    BetseCLI().run(["init", yml_file])

    # Simulate
    BetseCLI().run(["sim", yml_file])

    # Plot sim
    BetseCLI().run(["plot", "sim", yml_file])


def set_up_config(file_name, new_config=False):

    BetseMetaApp()

    if new_config:
        BetseCLI().run(["config", file_name])

    with open(file_name) as f:
        config = yaml.load(f)

    #### Configure yaml parameters ###

    # Set up experiment time
    config["sim time settings"]["time step"] = 1e-3
    config["sim time settings"]["total time"] = 1.0
    config["sim time settings"]["sampling rate"] = 5e-3

    # Set up NA change parameters
    na_multiplier = 9.0
    config["change Na mem"]['event happens'] = True
    config["change Na mem"]['multiplier'] = na_multiplier

    # Set up change parameters
    k_multiplier = 68.0
    config["change K mem"]['event happens'] = True
    config["change K mem"]['multiplier'] = k_multiplier

    # Set up change parameters
    cl_multiplier = 6.0
    config["change Cl mem"]['event happens'] = True
    config["change Cl mem"]['multiplier'] = cl_multiplier

    with open(file_name, "w") as f:
        yaml.dump(config, f)


def get_cells(results_path):
    cell_list = []
    with open(results_path) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            cell_list.append(row)

    return cell_list


def main():

    file_name = "SimTest/test1.yml"

    set_up_config(file_name, new_config=True)

    run_exp(file_name)

    results_path = "SimTest/RESULTS/sim_1/Vmem2D_TextExport/Vmem2D_0.csv"
    cells = get_cells(results_path)


if __name__ == '__main__':
    main()