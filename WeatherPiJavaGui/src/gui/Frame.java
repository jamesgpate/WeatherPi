package gui;

import javax.swing.JFrame;

public class Frame {
	public static void main(String[] whateverYouWantItToBe){
		JFrame f = new JFrame("The Weather");
		Canvas c = new Canvas();

		f.setSize(1280, 720);
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setLocationRelativeTo(null);
		
		f.add(c);
	}
}
