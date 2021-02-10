"""
This project produces a control heatmap for a chess game which shows which side
controls which squares how many times per ply/move in a Chess board
"""
from chess_heatmap_qxf2.chess_control_heatmap import ChessControlHeatmap

def main():
    control_heatmap = ChessControlHeatmap()
    control_heatmap.generate_heatmap_images()

if __name__ == "__main__":
    main()
    print("Please check the resource->output folder to view the heatmap")    