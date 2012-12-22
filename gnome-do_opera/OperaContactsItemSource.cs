/* OperaBookmarkItemSource.cs
 * Falko Krause
 * gmcs -target:library -r:System -r:/usr/lib/gnome-do/Do.Addins OperaBookmarkItemSource.cs
 */

using System;
using System.IO;
using System.Xml;
using System.Collections.Generic;

using Do.Addins;
using Do.Universe;

namespace Opera 
{

	public class OperaBookmarkItemSource : IItemSource
	{
		List<IItem> items;

		public OperaBookmarkItemSource ()
		{
			items = new List<IItem> ();
		}

		public string Name { get { return "Opera Bookmarks"; } }
		public string Description { get { return "Indexes your Opera bookmarks."; } }
		public string Icon { get { return "gnome-web-browser"; } }

		public Type[] SupportedItemTypes
		{
			get {
				return new Type[] {
					typeof (BookmarkItem),
				};
			}
		}

		public ICollection<IItem> Items
		{
			get { return items; }
		}

		public ICollection<IItem> ChildrenOfItem (IItem parent)
		{
			return null;	
		}
		public void UpdateItems ()
		{
			string home = Environment.GetFolderPath (Environment.SpecialFolder.Personal);
			string bookmarks_file = "~/.opera/contacts.adr".Replace ("~", home);


			items.Clear ();
			try {
				StreamReader re = File.OpenText(bookmarks_file);
				string input = null;
				string title = null;
				string link = null;
				while ((input = re.ReadLine()) != null)
				{
					if (input.Contains("#CONTACT")){
						while ((input = re.ReadLine()) != null){
							if (input.Contains("MAIL=")){ link=input.Substring(5);}
							if (input.Contains("NAME=")){ title=input.Substring(6);}
							if (input.Contains("ICON")){break;}
						}
						items.Add (new BookmarkItem (title,link));
					}

				}
				re.Close();
			} catch (Exception e) {
				Console.Error.WriteLine ("Could not read Opera Bookmarks file {0}: {1}",
						bookmarks_file, e.Message);
			}
		}

	}
}

