from shared.contract import Block


def render(blocks: list[Block]) -> str:
    if not blocks:
        return "No tasks scheduled."

    header = f"{'Task':<20} {'Importance':>10} {'Hours':>6} {'Deadline':>12}"
    line = "-" * len(header)
    rows = [header, line]

    for b in blocks:
        t = b.task
        rows.append(
            f"{t.title:<20} {t.importance:>10} {b.hours:>6.1f} {t.deadline.isoformat():>12}"
        )

    total = sum(b.hours for b in blocks)
    rows.append(line)
    rows.append(f"{'Total':<20} {'':>10} {total:>6.1f}")
    return "\n".join(rows)