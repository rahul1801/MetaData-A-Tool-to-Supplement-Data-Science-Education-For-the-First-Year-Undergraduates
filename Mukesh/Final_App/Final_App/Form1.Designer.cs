namespace Final_App
{
	partial class Final_App
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.panel2 = new System.Windows.Forms.Panel();
			this.panel1 = new System.Windows.Forms.Panel();
			this.startButton = new System.Windows.Forms.Button();
			this.enterUrlButton = new System.Windows.Forms.Button();
			this.urlTextBox = new System.Windows.Forms.TextBox();
			this.welcomeLabel = new System.Windows.Forms.Label();
			this.panel2.SuspendLayout();
			this.panel1.SuspendLayout();
			this.SuspendLayout();
			// 
			// panel2
			// 
			this.panel2.Controls.Add(this.enterUrlButton);
			this.panel2.Controls.Add(this.urlTextBox);
			this.panel2.Controls.Add(this.welcomeLabel);
			this.panel2.Location = new System.Drawing.Point(2, 1);
			this.panel2.Name = "panel2";
			this.panel2.Size = new System.Drawing.Size(798, 423);
			this.panel2.TabIndex = 0;
			// 
			// panel1
			// 
			this.panel1.Controls.Add(this.startButton);
			this.panel1.Location = new System.Drawing.Point(2, 1);
			this.panel1.Name = "panel1";
			this.panel1.Size = new System.Drawing.Size(798, 423);
			this.panel1.TabIndex = 1;
			// 
			// startButton
			// 
			this.startButton.AutoSize = true;
			this.startButton.Location = new System.Drawing.Point(328, 194);
			this.startButton.Name = "startButton";
			this.startButton.Size = new System.Drawing.Size(75, 27);
			this.startButton.TabIndex = 2;
			this.startButton.Text = "Start";
			this.startButton.UseVisualStyleBackColor = true;
			this.startButton.Click += new System.EventHandler(this.startButton_Click);
			// 
			// enterUrlButton
			// 
			this.enterUrlButton.AutoSize = true;
			this.enterUrlButton.Location = new System.Drawing.Point(148, 109);
			this.enterUrlButton.Name = "enterUrlButton";
			this.enterUrlButton.Size = new System.Drawing.Size(75, 27);
			this.enterUrlButton.TabIndex = 2;
			this.enterUrlButton.Text = "Next";
			this.enterUrlButton.UseVisualStyleBackColor = true;
			this.enterUrlButton.Click += new System.EventHandler(this.enterUrlButton_Click);
			// 
			// urlTextBox
			// 
			this.urlTextBox.Location = new System.Drawing.Point(13, 110);
			this.urlTextBox.Name = "urlTextBox";
			this.urlTextBox.ScrollBars = System.Windows.Forms.ScrollBars.Horizontal;
			this.urlTextBox.Size = new System.Drawing.Size(100, 22);
			this.urlTextBox.TabIndex = 1;
			// 
			// welcomeLabel
			// 
			this.welcomeLabel.AutoSize = true;
			this.welcomeLabel.Location = new System.Drawing.Point(10, 68);
			this.welcomeLabel.Name = "welcomeLabel";
			this.welcomeLabel.Size = new System.Drawing.Size(97, 17);
			this.welcomeLabel.TabIndex = 0;
			this.welcomeLabel.Text = "welcomeLabel";
			// 
			// Final_App
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.AutoScroll = true;
			this.AutoSize = true;
			this.ClientSize = new System.Drawing.Size(800, 450);
			this.Controls.Add(this.panel1);
			this.Controls.Add(this.panel2);
			this.Name = "Final_App";
			this.Text = "Final_App";
			this.Load += new System.EventHandler(this.Final_App_Load);
			this.panel2.ResumeLayout(false);
			this.panel2.PerformLayout();
			this.panel1.ResumeLayout(false);
			this.panel1.PerformLayout();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.Panel panel2;
		private System.Windows.Forms.Label welcomeLabel;
		private System.Windows.Forms.TextBox urlTextBox;
		private System.Windows.Forms.Button enterUrlButton;
		private System.Windows.Forms.Panel panel1;
		private System.Windows.Forms.Button startButton;
	}
}

