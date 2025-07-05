import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_figure(results_path, output_path):
    # 1. Load data
    df = pd.read_csv(results_path)

    # 2. Create combined LLM_method column
    if 'method' in df.columns:
        df['LLM_method'] = df['LLM'] + '_' + df['method']
    else:
        df['LLM_method'] = df['LLM']

    # 3. Pivot the table to prepare the heatmap
    pivot = df.pivot(index='column', columns='LLM_method', values='mean_similarity')

    # 3a. Clip values to [0, 1]
    pivot = pivot.clip(0.0, 1.0)

    # 4. Draw the heatmap with fixed color range 0→1
    fig, ax = plt.subplots(figsize=(14, 8))
    im = ax.imshow(pivot.values, aspect='auto', cmap='viridis', vmin=0.0, vmax=1.0)

    # 5. Annotate each cell with its value (two decimals)
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            val = pivot.values[i, j]
            # choose text color for contrast
            text_color = 'white' if val < 0.5 else 'black'
            ax.text(j, i, f"{val:.2f}", ha='center', va='center', color=text_color, fontsize=8)

    # 6. Configure ticks, labels, and title
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=45, ha='right')
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_xlabel('LLM')
    ax.set_ylabel('Task')
    ax.set_title('Mean Similarity Heatmap Task VS LLM')

    # 7. Add color bar with ticks from 0 to 1 in steps of 0.1
    cbar = plt.colorbar(im, ax=ax, orientation='vertical', pad=0.02)
    cbar.set_label('Mean Similarity', rotation=270, labelpad=15)
    cbar.set_ticks(np.arange(0.0, 1.01, 0.1))

    # 8. Save the figure as a PNG
    plt.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)

    print(f"Heatmap saved to '{output_path}'")