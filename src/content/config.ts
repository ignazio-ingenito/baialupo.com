import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
	type: 'content',
	// Type-check frontmatter using a schema
	schema: z.object({
		description: z.string(),
		// Transform string to Date object
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		heroImage: z.string().optional(),
		// baialupo posts
		id: z.number().optional(),
		title: z.string().optional(),
		alias: z.string().optional(),
		category: z.string().optional(),
		featured: z.boolean().optional(),
		created: z.coerce.date().optional(),
		modified: z.coerce.date().optional(),
		created_by: z.string().optional(),
	}),
});

export const collections = { blog };
