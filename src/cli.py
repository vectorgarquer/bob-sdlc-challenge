#!/usr/bin/env python3
"""
cli.py — Interfaz de línea de comandos de NeoTracker.

Uso:
    python cli.py fetch --start 2025-01-01 --end 2025-01-07
    python cli.py fetch --start 2025-01-01 --end 2025-01-07 --sort size
    python cli.py fetch --start 2025-01-01 --end 2025-01-07 --sort velocity
    python cli.py danger --start 2025-01-01 --end 2025-01-07
    python cli.py watch add <neo_id> --start 2025-01-01 --end 2025-01-07
    python cli.py watch remove <neo_id>
    python cli.py watch list
"""
import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from nasa_client import fetch_neos
from analyzer import sort_by_size, sort_by_velocity, find_most_dangerous
from watchlist_service import add_to_watchlist, remove_from_watchlist, list_watchlist, get_watchlist
from models import WatchList, NearEarthObject


def cmd_fetch(args):
    neos = fetch_neos(args.start, args.end, args.key)
    if args.sort == "size":
        neos = sort_by_size(neos, descending=True)
    elif args.sort == "velocity":
        neos = sort_by_velocity(neos, descending=False)

    print(f"\n📡 {len(neos)} NEOs encontrados ({args.start} → {args.end})\n")
    for neo in neos:
        hazard = "⚠️ " if neo.is_potentially_hazardous else "   "
        print(
            f"{hazard}{neo.name:<40} "
            f"Ø {neo.estimated_diameter_km_avg:.4f} km  "
            f"vel {neo.relative_velocity_kmh:>10.0f} km/h  "
            f"dist {neo.miss_distance_km:>14.0f} km  "
            f"{neo.close_approach_date}"
        )


def cmd_danger(args):
    neos = fetch_neos(args.start, args.end, args.key)
    most_dangerous = find_most_dangerous(neos)
    print(f"\n☄️  Asteroide más peligroso ({args.start} → {args.end}):\n")
    print(json.dumps(most_dangerous.to_dict(), indent=2, ensure_ascii=False))


def cmd_watch_add(args):
    neos = fetch_neos(args.start, args.end, args.key)
    neo_map = {n.neo_id: n for n in neos}
    if args.neo_id not in neo_map:
        print(f"❌ NEO '{args.neo_id}' no encontrado en el rango {args.start} → {args.end}")
        sys.exit(1)
    result = add_to_watchlist(neo_map[args.neo_id])
    icon = "✅" if result["status"] == "added" else "⚠️ "
    print(f"{icon} {result['status'].upper()}: {result['name']} ({result['id']})")


def cmd_watch_remove(args):
    result = remove_from_watchlist(args.neo_id)
    icon = "✅" if result["status"] == "removed" else "❌"
    print(f"{icon} {result['status'].upper()}: {result['id']}")


def cmd_watch_list(_args):
    items = list_watchlist()
    if not items:
        print("📋 Lista de seguimiento vacía.")
        return
    print(f"\n📋 Lista de seguimiento ({len(items)} asteroides):\n")
    for item in items:
        print(json.dumps(item, indent=2, ensure_ascii=False))


def build_parser():
    parser = argparse.ArgumentParser(
        prog="neotracker",
        description="🛰️  NeoTracker — Centro de Monitoreo de Objetos Cercanos a la Tierra",
    )
    parser.add_argument("--key", default="DEMO_KEY", help="NASA API key (default: DEMO_KEY)")
    sub = parser.add_subparsers(dest="command", required=True)

    # fetch
    p_fetch = sub.add_parser("fetch", help="Consultar asteroides en un rango de fechas")
    p_fetch.add_argument("--start", required=True, help="Fecha inicio YYYY-MM-DD")
    p_fetch.add_argument("--end", required=True, help="Fecha fin YYYY-MM-DD")
    p_fetch.add_argument("--sort", choices=["size", "velocity"], default=None,
                         help="Ordenar por tamaño o velocidad")

    # danger
    p_danger = sub.add_parser("danger", help="Identificar el asteroide más peligroso")
    p_danger.add_argument("--start", required=True, help="Fecha inicio YYYY-MM-DD")
    p_danger.add_argument("--end", required=True, help="Fecha fin YYYY-MM-DD")

    # watch
    p_watch = sub.add_parser("watch", help="Gestión de lista de seguimiento")
    watch_sub = p_watch.add_subparsers(dest="watch_cmd", required=True)

    pw_add = watch_sub.add_parser("add", help="Agregar asteroide a la lista")
    pw_add.add_argument("neo_id", help="ID del NEO a agregar")
    pw_add.add_argument("--start", required=True, help="Fecha inicio para buscar el NEO")
    pw_add.add_argument("--end", required=True, help="Fecha fin para buscar el NEO")

    pw_rem = watch_sub.add_parser("remove", help="Eliminar asteroide de la lista")
    pw_rem.add_argument("neo_id", help="ID del NEO a eliminar")

    watch_sub.add_parser("list", help="Ver lista de seguimiento")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "fetch": cmd_fetch,
        "danger": cmd_danger,
    }

    if args.command in dispatch:
        dispatch[args.command](args)
    elif args.command == "watch":
        watch_dispatch = {
            "add": cmd_watch_add,
            "remove": cmd_watch_remove,
            "list": cmd_watch_list,
        }
        watch_dispatch[args.watch_cmd](args)


if __name__ == "__main__":
    main()
