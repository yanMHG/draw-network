import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap


def geoDrawNetwork(
    locations,  # dict node -> (lat, lon)
    edges_ij,  # dict (node_i, node_j) -> value
    edges_jk,  # dict (node_j, node_k) -> value
    edges_ij_color="gray",
    edges_jk_color="orange",
    node_color="red",
    self_loop_shift=350000,
    font_size=6,
):
    m = Basemap(
        projection="merc",
        llcrnrlon=min([v[1] for v in locations.values()]) - 1,
        llcrnrlat=min([v[0] for v in locations.values()]) - 1,
        urcrnrlon=max([v[1] for v in locations.values()]) + 1,
        urcrnrlat=max([v[0] for v in locations.values()]) + 1,
        lat_ts=0,
        resolution="i",
        suppress_ticks=True,
    )

    # convert lat/lon to xy
    lons_xy_vals, lats_xy_vals = m(
        [v[1] for v in locations.values()], [v[0] for v in locations.values()],
    )
    lats_xy = {k: lats_xy_vals[i] for i, k in enumerate(locations.keys())}
    lons_xy = {k: lons_xy_vals[i] for i, k in enumerate(locations.keys())}
    positions_xy = {k: (lons_xy[k], lats_xy[k]) for k in locations.keys()}

    G = nx.DiGraph()
    for (node_i, node_j), value in edges_ij.items():
        G.add_edge(node_i, node_j, flow=value, color=edges_ij_color)
    for (node_j, node_k), value in edges_jk.items():
        G.add_edge(node_j, node_k, flow=value, color=edges_jk_color)

    nx.draw_networkx(
        G,
        positions_xy,
        node_color=node_color,
        font_size=font_size,
        edge_color=nx.get_edge_attributes(G, "color").values(),
    )

    for e in G.edges():
        if e[0] != e[1]:
            positions = positions_xy
        else:
            positions = {
                k: (v[0], v[1] + self_loop_shift) for k, v in positions_xy.items()
            }
        nx.draw_networkx_edge_labels(
            G,
            positions,
            edge_labels={e: nx.get_edge_attributes(G, "flow")[e]},
            bbox=dict(fc=nx.get_edge_attributes(G, "color")[e], ec="none", pad=1),
            verticalalignment="top",
            rotate=False,
            font_size=font_size,
        )

    m.bluemarble()
    m.drawcountries()
    plt.show()


def geoBrazilUFDrawNetwork(
    edges_ij,  # dict (node_i, node_j) -> value
    edges_jk,  # dict (node_j, node_k) -> value
    edges_ij_color="gray",
    edges_jk_color="orange",
    node_color="red",
    self_loop_shift=350000,
    font_size=6,
):
    locations = {
        "AC": (-8.77, -70.55),
        "AL": (-9.71, -35.73),
        "AM": (-3.07, -61.66),
        "AP": (1.41, -51.77),
        "BA": (-12.96, -38.51),
        "CE": (-3.71, -38.54),
        "DF": (-15.83, -47.86),
        "ES": (-19.19, -40.34),
        "GO": (-16.64, -49.31),
        "MA": (-2.55, -44.30),
        "MT": (-12.64, -55.42),
        "MS": (-20.51, -54.54),
        "MG": (-18.10, -44.38),
        "PA": (-5.53, -52.29),
        "PB": (-7.06, -35.55),
        "PR": (-24.89, -51.55),
        "PE": (-8.28, -35.07),
        "PI": (-8.28, -43.68),
        "RJ": (-22.84, -43.15),
        "RN": (-5.22, -36.52),
        "RO": (-11.22, -62.80),
        "RS": (-30.01, -51.22),
        "RR": (1.89, -61.22),
        "SC": (-27.33, -49.44),
        "SE": (-10.90, -37.07),
        "SP": (-23.55, -46.64),
        "TO": (-10.25, -48.25),
    }
    geoDrawNetwork(
        locations,
        edges_ij,
        edges_jk,
        edges_ij_color=edges_ij_color,
        edges_jk_color=edges_jk_color,
        node_color=node_color,
        self_loop_shift=self_loop_shift,
        font_size=font_size,
    )
