using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Final_App
{
	public partial class Form2 : Form
	{
		public Form2()
		{
			InitializeComponent();
			// write scatter matrix picture
			scatterMatrixImage.Image = Image.FromFile("E:\\IBM\\Mukesh\\images\\scatter_matrix.png");
			scatterMatrixImage.SizeMode = PictureBoxSizeMode.StretchImage;
		}

		private void closeButton_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.Cancel;
		}


	}
}
