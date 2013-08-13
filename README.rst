============
Introduction
============

A set of behaviors that are assignable to custom dexterity types for complex system setups. Assign the behavior
to a specific type to have it purge parents, children, siblings, or site root each time it is edited. This is 
an advanced product, so please do not use unless you fully understand the implications of caching.

NOTE: The purge behaviors are additive. If you purge something that has a purge behavior on it, it will be
triggered. If you are not careful, this could end in an infinite loop (e.g. purging parents on and item 
that purges siblings). There is no support to stop this use case at the moment. If someone wanted to add this, 
it would be very awesome of you. Otherwise, this will manifest as a max recursion error. 


Usage
-----

To use, add collective.purge_behaviors to the list of eggs in your plone site and then activate the behavior
in the dexterity control panel for the type that should exhibit the purge behavior. 

HINT: If these instructions don't make sense to you, you shouldn't be using this product.


Purge Behaviors
---------------

This package provides 4 different kinds of purge behaviors. They are all triggered when an item is
edited, NOT when they are added for the first time. 

*Parents*: When this item is edited, purge its parents, one level up. This calls the adapter for each parent
so if the parents have the purge parent enabled as well, then it will keep going up the chain. This would be
ideal for a situation where you have a folder view that you want to aggressively cache, and anytime you add 
a new item to the folder you want that cache to be cleared. Think: news items.

*Siblings*: When this item is edited, purge anything in the same folder as the item. If those items have 
purge behaviors as well, they will be persisted. This is ideal for a custom view that lists the contents of
a parent folder in a portlet or something of that nature. Think: portlet and folder listings.

*Contents*: When this item is edited, purge anything it is containing. If that item is not folderish (that 
is, it implements IFolderish) then it will be bypassed for your safety. This is ideal for a custom view on 
the contents of a folder that rely on properties from the containing folder.

*Site Root*: When this item is edited, purge the site root. This is ideal for editing items that affect a 
front page display. For example, you add a custom donor type and there is a view on the front page that 
lists new donors. This will purge the plain views and the folder_listing of root.
