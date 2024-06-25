import { z, defineCollection } from 'astro:content'

const posts = defineCollection({
	type: 'content',
	schema: z.object({
		id: z.number(),
		title: z.string(),
		category: z.string(),
		featured: z.number().optional().default(0),
		image: z.string().optional(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	}),
})

const meteo = defineCollection({
	type: 'content',
	schema: z.object({
		title: z.string().optional(),
		pics: z.array(z.string()),
	})
})

const market = defineCollection({
	type: 'content',
	schema: z.object({
		id: z.number(),
		title: z.string(),
		description: z.string(),
		image: z.string().optional(),
		featured: z.number().optional().default(0),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	})
})

export const collections = {
	posts,
	meteo,
	market
}
