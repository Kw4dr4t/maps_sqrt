import osmnx as ox

latitude = float(input('Latitude:'))
longitude = float(input('Longitude:'))
point = (latitude, longitude)
G = ox.graph_from_point(
    point, dist=10000, retain_all=True, simplify=True, network_type="all"
)

u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)


roadColors = []
roadWidths = []

for item in data:
    if "length" in item.keys():
        if item["length"] <= 100:
            linewidth = 0.10
            color = "#a6a6a6"

        elif item["length"] <= 200:
            linewidth = 0.15
            color = "#676767"

        elif item["length"] <= 400:
            linewidth = 0.25
            color = "#454545"

        elif item["length"] <= 800:
            color = "#d5d5d5"
            linewidth = 0.35
        else:
            color = "#ededed"
            linewidth = 0.45
    else:
        color = "#a6a6a6"
        linewidth = 0.10

    roadColors.append(color)
    roadWidths.append(linewidth)


# Center of map
# latitude = 52.239583153299286
# longitude = 21.02479668643565

bgcolor = "#061529"

fig, ax = ox.plot_graph(
    G,
    node_size=0,
    figsize=(40, 60),
    dpi=1200,
    bgcolor=bgcolor,
    save=False,
    edge_color=roadColors,
    edge_linewidth=roadWidths,
    edge_alpha=1,
)


fig.tight_layout(pad=0)
fig.savefig(
    "roadMap.png",
    dpi=1200,
    bbox_inches="tight",
    format="png",
    facecolor=fig.get_facecolor(),
    transparent=False,
)
